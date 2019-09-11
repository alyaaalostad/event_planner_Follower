from rest_framework import serializers
from events.models import Event, UserEvent
from django.contrib.auth.models import User


class DisplayEventListSerializer(serializers.ModelSerializer):
	capacity = serializers.SerializerMethodField()
	class Meta:
		model= Event
		exclude=['organizer']

	def get_capacity(self, obj):
		total=0
		for x in obj.bookings.all():
			print(x)
			total += x.seats
		return obj.capacity - total

class CreateEventSerializer(serializers.ModelSerializer):
	class Meta:
		model= Event
		exclude=['organizer']



class BookingListSerializer(serializers.ModelSerializer):
	event = serializers.SerializerMethodField()
	
	class Meta:
		model= UserEvent
		exclude=['name',]

	def get_event(self, obj):
		return (obj.event.title)



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['first_name', 'last_name',]

class OrganizerListSerializer(serializers.ModelSerializer):
	organizer_name = serializers.SerializerMethodField()

	class Meta:
		model= Event
		fields=['organizer_name','title', 'date','time','location', 'capacity', 'event_image']

	def get_organizer_name(self, obj):
		return (obj.organizer.first_name+" "+obj.organizer.last_name)

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'password',]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        firstname = validated_data['first_name']
        lastname = validated_data['last_name']
        new_user = User(username=username, first_name=firstname, last_name=lastname)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class AttendeesSerializer(serializers.ModelSerializer):
	name=serializers.SerializerMethodField()

	class Meta:
		model= UserEvent
		fields=['name']

	def get_name(self, obj):
		return (obj.name.first_name+" "+obj.name.last_name)

class EventAttendeesSerializer(serializers.ModelSerializer):
		attendees=serializers.SerializerMethodField()
		class Meta:
			model=Event
			fields=['title', 'date', 'time', 'attendees',]

		def get_attendees(self,obj):
			myevent = obj.bookings.all()
			return AttendeesSerializer(myevent,many=True).data


