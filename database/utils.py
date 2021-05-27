from .models import BlogRecord
from .serializer import BlogRecordSerializer

class DataBaseAPI:
    def __init__(self):
        self.records = BlogRecord.objects.all()
        self.serializer = BlogRecordSerializer

    def record_all(self):
        records = self.records.all()
        records_serializer = self.serializer(records, many=True)
        return records_serializer.data

    def record_id(self, id):
        record = self.records.get(pk=id)
        if record:
            record_serializer = self.serializer(record)
            return record_serializer.data
        return None

    def record_delete(self, id, username):
        record = self.records.get(pk=id)
        if record.author == username:
            record.delete()
            return True
        else:
            return

    def record_create(self, data):
        data_serializer = self.serializer(data=data)
        if data_serializer.is_valid():
            BlogRecord(**data_serializer.data).save()
            return True
        return False

    def record_update(self, username, data):
        data_serializer = self.serializer(data=data)
        if data_serializer.is_valid():
            id = data_serializer.data['id']
            record = self.records.get(pk=id)
            if record.author != username:
                return False
            model = BlogRecord(**data_serializer.data)
            model.pk = id
            model.save()

            return True

        return False


