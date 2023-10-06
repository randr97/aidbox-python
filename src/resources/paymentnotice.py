from typing import Optional

from base import Reference
from base import Money
from base import Reference
from base import Reference
from base import Reference
from base import CodeableConcept
from base import Reference
from base import Identifier
from base import Reference
from base import DomainResource


class PaymentNotice(DomainResource):
	response: Optional[Reference] = None
	amount: Money
	request: Optional[Reference] = None
	payment: Reference
	recipient: Reference
	created: str
	paymentStatus: Optional[CodeableConcept] = None
	status: str
	payee: Optional[Reference] = None
	paymentDate: Optional[str] = None
	identifier: list[Identifier] = []
	provider: Optional[Reference] = None

