from connection import get_connection
from Beans.document import document


class documentDao:
    connection = get_connection

    def get_document_by_id(self, id):
        cur = self.connection.cursor()
        cur.execute(
            "select document_id,contenu from documents where document_id=%s", id)

        result = [document(id=item[0], contenu=item[1])
                  for item in cur.fetchall()]
        return result
