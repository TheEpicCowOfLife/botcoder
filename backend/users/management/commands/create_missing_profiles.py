from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile


class Command(BaseCommand):
    help = 'Creates missing profiles for users who do not have one'
    
    def handle(self, *args, **options):
        users_without_profiles = []
        
        for user in User.objects.all():
            try:
                # Check if profile exists
                user.profile
            except Profile.DoesNotExist:
                # Create a profile if it doesn't exist
                Profile.objects.create(user=user)
                users_without_profiles.append(user.username)
        
        if users_without_profiles:
            self.stdout.write(self.style.SUCCESS(
                f'Created profiles for {len(users_without_profiles)} users: {", ".join(users_without_profiles)}'
            ))
        else:
            self.stdout.write(self.style.SUCCESS('All users already have profiles')) 