"""The please-ack decorator to request acknowledgement."""

from typing import Sequence

import marshmallow.validate
from marshmallow import EXCLUDE, fields

from ..models.base import BaseModel, BaseModelSchema

ON = ("RECEIPT", "OUTCOME")


class PleaseAckDecorator(BaseModel):
    """Class representing the please-ack decorator."""

    class Meta:
        """PleaseAckDecorator metadata."""

        schema_class = "PleaseAckDecoratorSchema"

    def __init__(
        self,
        on: Sequence[str] = None,
    ):
        """
        Initialize a PleaseAckDecorator instance.

        Args:
            on: list of tokens describing circumstances for acknowledgement.

        """
        super().__init__()
        self.on = list(on) if on else None


class PleaseAckDecoratorSchema(BaseModelSchema):
    """PleaseAck decorator schema used in serialization/deserialization."""

    class Meta:
        """PleaseAckDecoratorSchema metadata."""

        model_class = PleaseAckDecorator
        unknown = EXCLUDE

    on = fields.List(
        fields.Str(metadata={"example": "OUTCOME"}),
        required=False,
        metadata={
            "description": "List of tokens describing circumstances for acknowledgement"
        },
        validate=marshmallow.validate.OneOf(["RECEIPT, OUTCOME"])
    )
