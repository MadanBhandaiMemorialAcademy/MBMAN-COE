
import os
import django
from django.test import Client
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.utils import setup_test_environment

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
setup_test_environment()

from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS += ['testserver']

from home.models import GalleryAlbum, GalleryImage

def test_bulk_actions():
    print("Testing bulk Move and Copy...")
    
    User = get_user_model()
    user, _ = User.objects.get_or_create(username='testadmin', email='test@example.com')
    if not user.is_staff:
        user.is_staff = True
        user.save()
    
    # Create albums
    album_source = GalleryAlbum.objects.create(title="Source Album")
    album_target = GalleryAlbum.objects.create(title="Target Album")
    
    valid_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00'
        b'\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'
    )
    
    img1 = GalleryImage.objects.create(album=album_source, caption="Image 1", image=SimpleUploadedFile("1.gif", valid_gif, "image/gif"))
    img2 = GalleryImage.objects.create(album=album_source, caption="Image 2", image=SimpleUploadedFile("2.gif", valid_gif, "image/gif"))
    
    client = Client()
    client.force_login(user)

    print("\n--- Testing COPY ---")
    # Copy img1 to target
    data_copy = {
        'action': 'copy',
        'image_ids': [img1.id],
        'target_album': album_target.id
    }
    client.post('/admin/gallery/bulk-action/', data_copy, follow=True)
    
    # Check Copy Results
    # img1 should still exist in source
    source_count = GalleryImage.objects.filter(album=album_source, caption="Image 1").count()
    # Should be 1 (original)
    if source_count == 1:
        print("PASS: Original image remains in source after copy.")
    else:
        print(f"FAIL: Source count after copy is {source_count} (expected 1)")

    # Target should have a copy
    target_count = GalleryImage.objects.filter(album=album_target, caption="Image 1").count()
    if target_count == 1:
        print("PASS: Image copied to target album.")
    else:
        print(f"FAIL: Target count after copy is {target_count} (expected 1)")


    print("\n--- Testing MOVE ---")
    # Move img2 to target
    data_move = {
        'action': 'move',
        'image_ids': [img2.id],
        'target_album': album_target.id
    }
    client.post('/admin/gallery/bulk-action/', data_move, follow=True)
    
    # Check Move Results
    # img2 should NOT be in source
    source_count_2 = GalleryImage.objects.filter(album=album_source, caption="Image 2").count()
    if source_count_2 == 0:
        print("PASS: Image removed from source after move.")
    else:
        print("FAIL: Image still in source after move.")

    # img2 should be in target
    target_count_2 = GalleryImage.objects.filter(album=album_target, caption="Image 2").count()
    if target_count_2 == 1:
        print("PASS: Image moved to target album.")
    else:
        print("FAIL: Image not found in target after move.")

    # Cleanup
    GalleryImage.objects.filter(album=album_source).delete()
    GalleryImage.objects.filter(album=album_target).delete()
    album_source.delete()
    album_target.delete()

if __name__ == "__main__":
    test_bulk_actions()
