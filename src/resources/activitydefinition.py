from typing import Optional

from base import Reference
from base import Range
from base import ContactDetail
from base import CodeableConcept
from base import Reference
from base import CodeableConcept
from base import CodeableConcept
from base import Reference
from base import Period
from base import UsageContext
from base import CodeableConcept
from base import BackboneElement
from base import ContactDetail
from base import BackboneElement
from base import CodeableConcept
from base import Identifier
from base import ContactDetail
from base import CodeableConcept
from base import Reference
from base import ContactDetail
from base import Quantity
from base import RelatedArtifact
from base import Reference
from base import ContactDetail
from base import Reference
from base import Period
from base import DomainResource


class ActivityDefinition(DomainResource):
	observationResultRequirement: list[Reference] = []
	timingRange: Optional[Range] = None
	description: Optional[str] = None
	date: Optional[str] = None
	transform: Optional[str] = None
	endorser: list[ContactDetail] = []
	publisher: Optional[str] = None
	approvalDate: Optional[str] = None
	jurisdiction: list[CodeableConcept] = []
	dosage: list[str] = []
	observationRequirement: list[Reference] = []
	purpose: Optional[str] = None
	subjectCodeableConcept: Optional[CodeableConcept] = None
	productCodeableConcept: Optional[CodeableConcept] = None
	name: Optional[str] = None
	productReference: Optional[Reference] = None
	timingPeriod: Optional[Period] = None
	useContext: list[UsageContext] = []
	copyright: Optional[str] = None
	experimental: Optional[bool] = None
	topic: list[CodeableConcept] = []
	participant: list[BackboneElement] = []
	title: Optional[str] = None
	library: list[str] = []
	author: list[ContactDetail] = []
	timingDateTime: Optional[str] = None
	timingTiming: Optional[str] = None
	usage: Optional[str] = None
	timingDuration: Optional[str] = None
	priority: Optional[str] = None
	status: str
	subtitle: Optional[str] = None
	kind: Optional[str] = None
	dynamicValue: list[BackboneElement] = []
	url: Optional[str] = None
	code: Optional[CodeableConcept] = None
	identifier: list[Identifier] = []
	lastReviewDate: Optional[str] = None
	editor: list[ContactDetail] = []
	doNotPerform: Optional[bool] = None
	bodySite: list[CodeableConcept] = []
	timingAge: Optional[str] = None
	intent: Optional[str] = None
	specimenRequirement: list[Reference] = []
	reviewer: list[ContactDetail] = []
	quantity: Optional[Quantity] = None
	version: Optional[str] = None
	relatedArtifact: list[RelatedArtifact] = []
	location: Optional[Reference] = None
	contact: list[ContactDetail] = []
	subjectReference: Optional[Reference] = None
	profile: Optional[str] = None
	effectivePeriod: Optional[Period] = None

