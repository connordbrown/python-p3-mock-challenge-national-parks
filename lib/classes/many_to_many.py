class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (not hasattr(self, 'name') and isinstance(name, str) and len(name) >= 3):
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set(trip.visitor for trip in Trip.all if trip.national_park == self))
    
    def total_visits(self):
        if self.trips():
            return len(self.trips())
        else:
            return 0
    
    def best_visitor(self):
        if self.visitors():
            visits = {}
            for tourist in self.visitors():
                visits[tourist] = len([visit for visit in self.trips() if visit.visitor == tourist])
            most_visits = max(visits.values())
            top_visitors = [tourist for tourist, count in visits.items() if count == most_visits]
            return top_visitors[0]
        else:
            return None
    
    @classmethod
    def most_visited(cls):
        visits = {}
        for park in cls.all:
            visits[park] = len(park.trips())
        most_visits = max(visits.values())
        top_visited = [park for park, count in visits.items() if count == most_visits]
        return top_visited[0] if top_visited else None

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date

class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set(trip.national_park for trip in Trip.all if trip.visitor == self))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in park.trips() if trip.visitor == self])