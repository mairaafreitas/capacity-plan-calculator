from utils import SECONDS_PER_DAY


def calculate_rps(daily_active_users: int, requests_per_user: int, reads: int, writes: int):
    """Calculate the Requests Per Second (RPS)"""

    requests_per_day = daily_active_users * requests_per_user
    requests_per_second = round(requests_per_day / SECONDS_PER_DAY, 2)

    read_requests_per_second = round(requests_per_second * reads / (reads + writes), 2)
    write_requests_per_second = round(requests_per_second * writes / (reads + writes), 2)

    print("\n--------------------Results--------------------")
    print("======Requests======")
    print("Requests Per Second (RPS) = Daily Active Users * Requests Per User / Seconds Per Day")
    print(f"The Requests Per Day is: {requests_per_day} requests")
    print(f"The Requests Per Second (RPS) is: {requests_per_second}rps")
    print(f"Read Requests Per Second is: {read_requests_per_second}rps")
    print(f"Write Requests Per Second is: {write_requests_per_second}rps")
    return requests_per_second, write_requests_per_second
