from database import init_db, save_assessment, get_assessments

init_db()

save_assessment(
    "Car",
    20,
    250,
    "Non-Vegetarian",
    2,
    3200,
    65
)

print(get_assessments())