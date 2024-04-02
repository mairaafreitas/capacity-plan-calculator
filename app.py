from calculators.bandwith_calculator import calculate_bandwith
from calculators.requests_per_sec_calculator import calculate_rps

from calculators.storage_calculator import calculate_storage

print("\nWelcome to the Capacity Plan Calculator")

print("\nLet's plan together? We are going to calculate:")
print("- Requests Per Second (RPS)")
print("- Read/Write Requests Per Second (RPS)")
print("- Bandwith required for the requests")
print("- Storage")

while True:
    try:
        daily_active_users = int(input("\nEnter the Daily Active Users (DAU): "))
        requests_per_user = int(input("Enter the total Requests per user: "))
        reads_and_writes = input("Enter the Reads vs Writes proportion (e.g: 9:1): ")
        request_size = int(input("Request size (kb): "))
        replication_factor = int(input("Replication factor: "))

        reads, writes = map(int, reads_and_writes.split(":"))
        break
    except ValueError:
        print("Please enter valid numbers.")


requests_per_second, writes_per_second = calculate_rps(daily_active_users, requests_per_user, reads, writes)
calculate_bandwith(requests_per_second, request_size)
calculate_storage(writes_per_second, request_size, replication_factor)
