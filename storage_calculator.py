from utils import DAYS_OF_THE_YEAR
from utils import SECONDS_PER_DAY
from utils import gb_to_tb
from utils import kb_to_mb
from utils import mb_to_gb


def calculate_storage(writes_per_second: int, size_for_request: int, replication_factor: int):
    """Calculate the Storage required for the requests."""
    print("\n======Storage======")
    print("Storage Per Second = Writes per second * Average request size * Replication factor")

    storage_per_second_kbs = round(writes_per_second * size_for_request * replication_factor, 4)
    storage_per_second_mbs = round(kb_to_mb(storage_per_second_kbs), 4)
    storage_per_day_gb = round(mb_to_gb(storage_per_second_mbs * SECONDS_PER_DAY), 4)
    storage_per_year_tb = round(gb_to_tb(storage_per_day_gb * DAYS_OF_THE_YEAR), 4)

    print(f"Storage required for a second: {storage_per_second_kbs}kbs")
    print(f"Storage required for a second: {storage_per_second_mbs}mbs")
    print(f"Storage required for a day: {storage_per_year_tb}mbs")
    print(f"Storage required for a day: {storage_per_day_gb}gb")

