class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(), slug_field="name"
    )
    drone = serializers.SlugRelatedField(
        queryset=Drone.objects.all(), slug_field="name"
    )

    class Meta:
        model = Competition
        fields = (
            "url",
            "pk",
            "distance_in_feet",
            "distance_achievement_date",
            "pilot",
            "drone",
            )