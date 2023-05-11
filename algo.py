from dateutil.relativedelta import relativedelta
from datetime import datetime

subscription_model = {
    "periods": 12,  # Nombre total de périodes
    "period_type": "week"  # Type de période (jours, semaines, mois, années)
}

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)
next_invoice_date = datetime(2022, 1, 1)


def get_next_invoice_date(start, end, next, periods, type):

    new_date = relativedelta(next, start)
    last_days = (next - start).days

    if type == "day":
        print(f"periode n°: {last_days + 1}/{periods}")
    elif type == "week":
        print(f"periode n°: {int(last_days / 7) + 1}/{periods}")
    elif type == "month":
        print(
            f"periode n°: {new_date.years * 12 + new_date.months + 1}/{periods}")
    elif type == "year":
        print(f"periode n°: {new_date.years + 1}/{periods}")


get_next_invoice_date(start_date, end_date, next_invoice_date,
                      subscription_model["periods"], subscription_model["period_type"])
