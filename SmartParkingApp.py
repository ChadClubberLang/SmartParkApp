class ParkingZone:
    def __init__(self, zone_id):
        self.zone_id = zone_id
        self.is_occupied = False
        self.vehicle_id = None

    def check_in(self, vehicle_id):
        if not self.is_occupied:
            self.is_occupied = True
            self.vehicle_id = vehicle_id
            print(f"Vehicle {vehicle_id} checked into zone {self.zone_id}.")
        else:
            print(f"Zone {self.zone_id} is already occupied by vehicle {self.vehicle_id}.")

    def check_out(self):
        if self.is_occupied:
            print(f"Vehicle {self.vehicle_id} checked out from zone {self.zone_id}.")
            self.is_occupied = False
            self.vehicle_id = None
        else:
            print(f"Zone {self.zone_id} is already empty.")

    def __str__(self):
        return f"Zone {self.zone_id} - {'Occupied' if self.is_occupied else 'Available'}"


class ParkingLot:
    def __init__(self, start_zone='1a', end_zone='10a'):
        self.zones = self._generate_zones(start_zone, end_zone)

    def _generate_zones(self, start_zone, end_zone):
        zones = []
        start_num = int(start_zone[:-1])
        end_num = int(end_zone[:-1])
        for i in range(start_num, end_num + 1):
            zones.append(ParkingZone(f"{i}a"))
        return zones

    def check_in(self, zone_id, vehicle_id):
        for zone in self.zones:
            if zone.zone_id == zone_id:
                zone.check_in(vehicle_id)
                return
        print(f"Zone {zone_id} not found.")

    def check_out(self, zone_id):
        for zone in self.zones:
            if zone.zone_id == zone_id:
                zone.check_out()
                return
        print(f"Zone {zone_id} not found.")

    def display_zones(self):
        for zone in self.zones:
            print(zone)


def main():
    parking_lot = ParkingLot()

    while True:
        print("\nCurrent parking lot status:")
        parking_lot.display_zones()

        action = input("\nChoose an action: [check-in, check-out, quit]: ").strip().lower()

        if action == "quit":
            break
        elif action == "check-in":
            zone_id = input("Enter zone to check in (e.g., 1a): ").strip().lower()
            vehicle_id = input("Enter vehicle ID: ").strip().upper()
            parking_lot.check_in(zone_id, vehicle_id)
        elif action == "check-out":
            zone_id = input("Enter zone to check out (e.g., 1a): ").strip().lower()
            parking_lot.check_out(zone_id)
        else:
            print("Invalid action. Please choose 'check-in', 'check-out', or 'quit'.")


if __name__ == "__main__":
    main()
