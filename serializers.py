

from rest_framework import serializers


from api.models import Course,CourseDetail

class CourseMiodelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class CourseDetailMiodelSerializers(serializers.ModelSerializer):
    class Meta:
        model=CourseDetail
        fields="__all__"

    course_name=serializers.CharField(source="course.name")
    course_img=serializers.CharField(source="course.course_img")

    teachers=serializers.SerializerMethodField()
    def get_teachers(self,obj):
        temp=[]
        for i in obj.teachers.all():
            temp.append(i.name)
        return temp

    recommend_courses = serializers.SerializerMethodField()

    def get_recommend_courses(self, obj):
        temp = []
        for i in obj.recommend_courses.all():
            temp.append({
                "name":i.name,
                "pk":i.pk
            })
        return temp
