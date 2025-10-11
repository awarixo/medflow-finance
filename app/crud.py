from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

def get_invoice_by_id(db: Session, invoice_id: str):
    return db.query(models.Invoice).filter(models.Invoice.invoice_id == invoice_id).first()

def delete_invoice_by_invoice_id(db: Session, invoice_id: str):
    invoice = get_invoice_by_id(db, invoice_id)
    if invoice:
        db.delete(invoice)
        db.commit()
        return True
    return False

def get_billing_summary(db: Session):
    total = db.query(func.sum(models.InvoiceItem.amount)).scalar() or 0
    paid = (
        db.query(func.sum(models.InvoiceItem.amount))
        .join(models.Invoice)
        .filter(models.Invoice.status == "Paid")
        .scalar() or 0
    )
    unpaid = (
        db.query(func.sum(models.InvoiceItem.amount))
        .join(models.Invoice)
        .filter(models.Invoice.status == "Unpaid")
        .scalar() or 0
    )
    return {"total_revenue": total, "paid": paid, "unpaid": unpaid}