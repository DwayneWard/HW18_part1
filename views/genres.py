from flask_restx import Namespace, Resource

from models import Genre, GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    """
    Class-Based View для отображения жанров из БД.
    Реализовано:
    - отображение всех фильмов GET-запросом на /genres.
    """
    def get(self):
        """
        Метод реализует отправку GET-запроса на /genres.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        """
        all_directors = Genre.query.all()
        return genres_schema.dump(all_directors), 200


@genre_ns.route('/<gid>')
class GenreView(Resource):
    """
    Class-Based View для отображения конкретного режиссера из БД.
    Реализовано:
    - отображение данных о конкретном режиссере GET-запросом на /genres/id;
    """
    def get(self, gid):
        """
        Метод реализует отправку GET-запроса на /genres/id.
        :param gid: id жанра, информацию о котором нужно вытащить из БД.
        :return: Сериализованные данные в формате JSON и HTTP-код 200.
        В случае, если id нет в базе данных - пустая строка и HTTP-код 404.
        """
        genre_by_id = Genre.query.get(gid)
        if not genre_by_id:
            return '', 404
        return genre_schema.dump(genre_by_id), 200
