import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost', charset='utf8'):
        #Параметры соединения
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
        self.charset = charset

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        #Открытие соединения
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.db
            )

    def disconnect(self):
        #Закрытие соединения
        if self._connection:
            self._connection.close()


class Countries:

    def __init__(self, db_connection, country_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.country_name = country_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_countries (country_name) VALUES (%s);", (self.country_name))
        self.db_connection.commit()
        c.close()


class Actors:

    def __init__(self, db_connection, actor_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.actor_name = actor_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_actors (actor_name) VALUES (%s);", (self.actor_name))
        self.db_connection.commit()
        c.close()


class Filmmakers:

    def __init__(self, db_connection, filmmaker_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.filmmaker_name = filmmaker_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_filmmakers (filmmaker_name) VALUES (%s);", (self.filmmaker_name))
        self.db_connection.commit()
        c.close()


class Film_writers:

    def __init__(self, db_connection, film_writer_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.film_writer_name = film_writer_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_film_writers (film_writer_name) VALUES (%s);", (self.film_writer_name))
        self.db_connection.commit()
        c.close()


class Producers:

    def __init__(self, db_connection, producer_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.producer_name = producer_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_producers (producer_name) VALUES (%s);", (self.producer_name))
        self.db_connection.commit()
        c.close()


class Cameramen:

    def __init__(self, db_connection, cameraman_name):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.cameraman_name = cameraman_name

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_cameramen (cameraman_name) VALUES (%s);", (self.cameraman_name))
        self.db_connection.commit()
        c.close()


class Films:

    def __init__(self, db_connection, film_name, release_date, filmmaker_id, film_writer_id, producer_id, cameraman_id, country_id, box_office_results):
        #Сохранение соединения и данных
        self.db_connection = db_connection.connection
        self.film_name = film_name
        self.release_date = release_date
        self.filmmaker_id = filmmaker_id
        self.film_writer_id = film_writer_id
        self.producer_id = producer_id
        self.cameraman_id = cameraman_id
        self.country_id = country_id
        self.box_office_results = box_office_results

    def save(self):
        #Запись данных из объекта в запись БД
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_films (film_name, release_date, filmmaker_id, film_writer_id, producer_id, cameraman_id, country_id, box_office_results) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (self.film_name, self.release_date, self.filmmaker_id, self.film_writer_id, self.producer_id, self.cameraman_id, self.country_id, self.box_office_results))
        self.db_connection.commit()
        c.close()


class FilmsActors:
    def __init__(self, db_connection, film_id, actor_id):
        self.db_connection = db_connection.connection
        self.film_id = film_id
        self.actor_id = actor_id

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO db_app_films_in_the_lead_role (films_id, actors_id) VALUES (%s, %s);", (self.film_id, self.actor_id))
        self.db_connection.commit()
        c.close()


con = Connection(user='dbuser', password='123', db='films')

with con:
    country = Countries(con, 'Россия')
    country.save()
    actor = Actors(con, 'Данила Козловский')
    actor.save()
    filmmaker = Filmmakers(con, 'Андрей Кравчук')
    filmmaker.save()
    film_writer = Film_writers(con, 'Андрей Рубанов')
    film_writer.save()
    producer = Producers(con, 'Константин Эрнст')
    producer.save()
    cameraman = Cameramen(con, 'Игорь Гринякин')
    cameraman.save()
    film = Films(con, 'Викинг', '2016.12.29', '1', '1', '1', '1', '1', '27018393')
    film.save()
    film_actor = FilmsActors(con, '1', '1')
    film_actor.save()
