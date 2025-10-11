from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(String(20), unique=True, index=True, nullable=False)
    patient_id = Column(String(20), nullable=False)  # foreign key to patients.patient_id (varchar)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)  # 'Paid' or 'Unpaid'

    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False)
    service_name = Column(String(100), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    invoice = relationship("Invoice", back_populates="items")