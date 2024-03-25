class Classroom:
    classroom_list=None

    @staticmethod
    def search_classroom(class_room):
        for item in Classroom.classroom_list:
            if item.lower() == class_room.lower():
                return "Found"
        return -1

