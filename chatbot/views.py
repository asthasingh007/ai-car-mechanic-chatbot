from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ChatMessage, Diagnosis, Booking, MediaUpload
from .serializers import (
    ChatMessageSerializer,
    DiagnosisSerializer,
    BookingSerializer,
)


@api_view(["POST"])
def chat(request):
    serializer = ChatMessageSerializer(data=request.data)

    if serializer.is_valid():
        message = serializer.save()

        text = request.data.get("message", "").lower()

        reply = "Please provide more details about your car problem."

        if "overheat" in text or "hot" in text:
            reply = (
                "Your car may have a cooling-system issue. "
                "Please check the coolant level and radiator. "
                "Avoid driving if the engine temperature is very high."
            )

        elif "brake" in text:
            reply = (
                "There may be a brake-system issue. "
                "Please have the brake system checked by a mechanic."
            )

        elif "battery" in text or "start" in text:
            reply = (
                "The battery may be weak or discharged. "
                "Please check the battery terminals and battery charge."
            )

        elif "tyre" in text or "tire" in text:
            reply = (
                "Please check the tyre pressure and inspect "
                "the tyre for visible damage or a puncture."
            )

        return Response(
            {
                "reply": reply,
                "data": ChatMessageSerializer(message).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def diagnosis(request):
    serializer = DiagnosisSerializer(data=request.data)

    if serializer.is_valid():
        result = serializer.save()

        return Response(
            DiagnosisSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["POST"])
def booking(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        result = serializer.save()

        return Response(
            BookingSerializer(result).data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET"])
def get_booking(request, id):
    try:
        booking_data = Booking.objects.get(id=id)

    except Booking.DoesNotExist:
        return Response(
            {"error": "Booking not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    return Response(
        BookingSerializer(booking_data).data
    )


@api_view(["POST"])
def upload_media(request):
    file = request.FILES.get("file")
    media_type = request.data.get("media_type", "unknown")

    if not file:
        return Response(
            {"error": "Please upload a file."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    media = MediaUpload.objects.create(
        file=file,
        media_type=media_type,
    )

    return Response(
        {
            "message": "File uploaded successfully.",
            "id": media.id,
            "file": media.file.url,
            "media_type": media.media_type,
        },
        status=status.HTTP_201_CREATED,
    )