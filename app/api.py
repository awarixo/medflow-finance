from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/invoices", response_model=List[schemas.Invoice])
def list_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_invoices(db, skip=skip, limit=limit)

@router.get("/invoices/{invoice_id}", response_model=schemas.Invoice)
def get_invoice_details(invoice_id: str, db: Session = Depends(get_db)):
    invoice = crud.get_invoice_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: str, db: Session = Depends(get_db)):
    success = crud.delete_invoice_by_invoice_id(db, invoice_id)
    if not success:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"ok": True}

@router.get("/billing_summary", response_model=schemas.BillingSummary)
def billing_summary(db: Session = Depends(get_db)):
    return crud.get_billing_summary(db)