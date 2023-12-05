from rest_framework import serializers

from .models.publications import (
    ErpIncidentReport,
    ErpPublication,
    ErpPublicationCategorie,
    ErpPublicationComment,
    ErpPublicationReaction,
    ErpPublicationTag,
    ErpPublicationType,
)


class ErpPublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpPublicationType
        fields = "__all__"


class ErpPublicationCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpPublicationCategorie
        fields = "__all__"


class ErpPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpPublication
        fields = "__all__"


class ErpPublicationCommentSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ErpPublicationComment
        fields = "__all__"


class ErpIncidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpIncidentReport
        fields = "__all__"


class ErpPublicationReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpPublicationReaction
        fields = "__all__"


class ErpPublicationTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErpPublicationTag
        fields = "__all__"


class ErpPublicationDetaillsSerializer(serializers.HyperlinkedModelSerializer):
    category = ErpPublicationCategorieSerializer()
    publicaion_type = ErpPublicationTypeSerializer()
    comments = ErpPublicationCommentSerialiser()

    class Meta:
        model = ErpPublication
        fields = ["title", "client", "codument", "co_publisher", "caption", "publication_type", "category", "comments"]
