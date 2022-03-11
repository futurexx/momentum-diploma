import enum

from app import db


class Company(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))

    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'))

    def __repr__(self):
        return '<Company {}>'.format(self.name)


class Staff(db.Model):

    class StaffPositionEnum(enum.Enum):
        supervisor = 'supervisor'
        manager = 'manager'
        other = 'other'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.Date)

    position = db.Column(db.Enum(StaffPositionEnum), default=StaffPositionEnum.other, nullable=False)


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(100))
    age_rank = db.Column(db.Integer)  # Это поле должно быть числом?
    quality = db.Column(db.String(100))  # не разглядел слово на схеме но похоже на quality?
    # Может сделать для этого поля ограниченное число вариантов, как это сделано в поле Staff.position?


class Partner(db.Model):
    class PartnerTypesEnum(enum.Enum):
        manufacturer = 'manufacturer'
        auditor = 'auditor'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(PartnerTypesEnum), default=PartnerTypesEnum.auditor, nullable=False)
    info = db.Column(db.Text)
    contacts = db.Column(db.String(200))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


class Document(db.Model):
    class DocumentTypesEnum(enum.Enum):
        checklist = 'checklist'
        template = 'template'
        instruction = 'instruction'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(DocumentTypesEnum), default=DocumentTypesEnum.checklist, nullable=False)
    content = db.Column(db.Text)


class Check(db.Model):
    class CheckStatusEnum(enum.Enum):
        ready_to_check = 'ready_to_check'
        in_progress = 'in_progress'
        done = 'done'
        need_rework = 'need_rework'
        instruction = 'instruction'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('partner.id'))
    auditor_id = db.Column(db.Integer, db.ForeignKey('partner.id'))
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))
    status = db.Column(db.Enum(CheckStatusEnum), default=CheckStatusEnum.checklist, nullable=False)
