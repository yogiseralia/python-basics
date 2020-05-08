class Flight:

    def __init__(self, flightNo, aircraft):
        # we can define class invariants
        if not flightNo[:2].isalpha():
            raise ValueError(f"No airline code in '{flightNo}'")

        if not flightNo[:2].isupper():
            raise ValueError(f"Invalid airline code '{flightNo}'")

        if not (flightNo[2:].isdigit() and int(flightNo[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{flightNo}'")

        self._flightNo = flightNo
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._flightNo

    def airline(self):
        return self._flightNo[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate seat to a passenger

        :arg seat seat designator such as '12C' or '21F'.
        :arg passenger
        """
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat already occupied")

        self._seating[row][letter] = passenger

    def relocate_seat(self, from_seat, to_seat):
        """Relocates a passenger to a different seat.
        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} is already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            return ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An Iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def __init__(self, registration):
        Aircraft.__init__(self, registration)

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def __init__(self, registration):
        Aircraft.__init__(self, registration)

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # for sake of simplicity, we ignore
        # seating arrangement of first-class
        return range(1, 56), "ABCDEFGHK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name:{passenger}" \
             f"  Flight:{flight_number}" \
             f"  Seat:{seat}" \
             f"  Aircraft:{aircraft}" \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA786", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Yogesh Seralia")
    f.allocate_seat("12B", "Heena Seralia")
    f.allocate_seat("15F", "Pratap Singh Seralia")
    f.allocate_seat("15E", "Rani Seralia")
    f.allocate_seat("1C", "Ravi Vashishth")

    g = Flight("AF721", Boeing777("F-GSPS"))
    g.allocate_seat("55K", "Larry Wall")
    g.allocate_seat("33G", "Yushito Nakamura")
    g.allocate_seat("4B", "Brian Hansan")
    g.allocate_seat("15E", "Eva Mendis")
    g.allocate_seat("4A", "AB De Villiars")

    return f, g
