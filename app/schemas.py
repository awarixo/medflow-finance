from pydantic import BaseModel
from typing import List
from datetime import date
from decimal import Decimal

class InvoiceItemBase(BaseModel):
    service_name: str
    amount: Decimal

class InvoiceItem(InvoiceItemBase):
    id: int

    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    invoice_id: str
    patient_id: str  # shows both on UI
    date: date
    status: str  # 'Paid'/'Unpaid'

class Invoice(InvoiceBase):
    id: int
    items: List[InvoiceItem] = []

    class Config:
        orm_mode = True

# For summary endpoints:
class BillingSummary(BaseModel):
    total_revenue: Decimal
    paid: Decimal
    unpaid: Decimal