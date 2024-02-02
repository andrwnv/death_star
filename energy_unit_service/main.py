import asyncio

from service import run


SERVICE_INFO = """
    ______                                  __  __      _ __
   / ____/___  ___  _________ ___  __      / / / /___  (_) /_
  / __/ / __ \/ _ \/ ___/ __ `/ / / /_____/ / / / __ \/ / __/
 / /___/ / / /  __/ /  / /_/ / /_/ /_____/ /_/ / / / / / /_
/_____/_/ /_/\___/_/   \__, /\__, /      \____/_/ /_/_/\__/
                      /____//____/

Death-Star: Energy unit service (v1.0.0)
"""

if __name__ == "__main__":
    print(SERVICE_INFO)

    asyncio.run(run())
