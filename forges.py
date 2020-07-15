import random

from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func, select
from faker_vehicle import VehicleProvider
# fake.vehicle_make()
# # BMW
# fake.vehicle_model()
# # SL
# fake.vehicle_year()
# # 2008
# fake.vehicle_category()
# # Wagon
from server import db, migrate
# from app.models import ReservedCarStatus, resrvRecord, CarAllinfo, QueryRecord, OrderRecord
from server import EscooterAllinfo, CarAllinfo, FONLoc, RealtimeCarDetails, RealtimeCarOrderRecord, ReservedCarStatus, QueryRecord, BookingRecord, OrderRecord
from sqlalchemy import and_, func

fake = Faker()
fake.add_provider(VehicleProvider)


def fake_longnla():
    # for i in range(cnt):
    loc1 = FONLoc(
        loc=1,
        longnla=str("(25.016695, 121.543692)")
    )
    db.session.add(loc1)
    loc2 = FONLoc(
        loc=2,
        longnla=str("(25.021295, 121.539112)")
    )
    db.session.add(loc2)
    loc3 = FONLoc(
        loc=3,
        longnla=str("(25.019808, 121.541526)")
    )
    db.session.add(loc3)
    db.session.commit()


def fake_scooter(cnt=30):
    for i in range(cnt):
        car = EscooterAllinfo(price=random.randint(2, 7),
                              location=str("(25.019808, 121.541526)"),
                              UsedorNot=False)
        db.session.add(car)
    db.session.commit()


def fake_car(cnt=30):

    for i in range(cnt):
        car = CarAllinfo(bmid=1000021 + random.randint(1, 2),
                         sub_type=fake.vehicle_category(),
                         brand_id=fake.vehicle_make(),
                         model_id=fake.vehicle_model(),
                         price=random.randint(2, 7),
                         location=random.randint(1, 3),
                         UsedorNot=False)
        db.session.merge(car)
    db.session.commit()


def fake_car_status():
    time_slot = 10
    loc_list = []
    bm_list = []
    all_list = db.session.query(CarAllinfo).all()
    cnt_bm = db.session.query(CarAllinfo).group_by(
        CarAllinfo.bmid).count()  # having(func.count('*')
    bm_list_v = db.session.query(
        CarAllinfo.bmid).group_by(CarAllinfo.bmid).all()
    cnt_loc = db.session.query(CarAllinfo).group_by(
        CarAllinfo.location).count()
    loc_list_v = db.session.query(CarAllinfo).group_by(
        CarAllinfo.location).all()
    for i in loc_list_v:
        loc_list.append(i.location)
    for i in bm_list_v:
        bm_list.append(i.bmid)
    # print(cnt_bm, bm_list)
    # print(cnt_loc, loc_list)

    for i in range(1585134900, 1585134900 + 3600*time_slot, 3600):
        for j in loc_list:
            for k in bm_list:
                csta1 = ReservedCarStatus(
                    date=i,
                    location=j,
                    # db.session.query(CarAllinfo.location).order_by(func.random()).limit(1),
                    bmid=k,
                    # db.session.query(CarAllinfo.bmid).\
                    # filter(CarAllinfo.location == '1').order_by(
                    #     func.random()).limit(1),
                    carAmount=db.session.query(CarAllinfo.bmid).\
                    filter(and_(CarAllinfo.bmid == k, CarAllinfo.location == j)).count())
                db.session.add(csta1)

    db.session.commit()
