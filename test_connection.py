from sqlalchemy import text
from database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("✅ Database Connected Successfully!")
        print(result.fetchone())

except Exception as e:
    print("❌ Connection Failed")
    print(e)