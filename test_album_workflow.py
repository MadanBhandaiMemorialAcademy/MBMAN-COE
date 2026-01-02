
import os
import django
from django.test import Client
from django.contrib.auth import get_user_model
from django.test.utils import setup_test_environment

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
setup_test_environment()

from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS += ['testserver']

from home.models import GalleryAlbum, GalleryImage

def test_album_upload_workflow():
    print("Testing Album-First Upload Workflow...")
    
    User = get_user_model()
    user, _ = User.objects.get_or_create(username='testadmin', email='test@example.com')
    if not user.is_staff:
        user.is_staff = True
        user.save()
    
    # Create test album
    album = GalleryAlbum.objects.create(title="Workflow Test Album")
    
    client = Client()
    client.force_login(user)

    ### TEST 1: Check Form Rendering with Context ###
    print("\n[Test 1] GET gallery_add with album_id")
    response_get = client.get(f'/admin/gallery/add/?album_id={album.id}')
    
    # Check if target_album is in context
    if response_get.context['target_album'] == album:
        print("PASS: target_album context set correctly.")
    else:
        print("FAIL: target_album context missing or incorrect.")
    
    # Check if 'Target Album' text is in response (indicating visual feedback)
    if b'Target Album' in response_get.content and b'workflow test album' in response_get.content.lower():
         print("PASS: Target album title displayed in form.")
    else:
         print("FAIL: Target album title not found in form content.")

    ### TEST 2: Submit Form with Implicit Album ###
    print("\n[Test 2] POST gallery_add with implicit album")
    
    with open('test_image_workflow.gif', 'wb') as f:
        f.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b')
        
    with open('test_image_workflow.gif', 'rb') as img:
        data = {
            'album': album.id, # The hidden input submits this
            'image': img,
            'caption': 'Workflow Test Image',
            'is_spotlight': False,
            'is_cover': False,
            'display_order': 0
        }
        # We append ?album_id to URL to trigger the redirect behavior back to filtered list
        response_post = client.post(f'/admin/gallery/add/?album_id={album.id}', data, follow=True)
    
    # Check redirection
    redirect_chain = response_post.redirect_chain
    print(f"Redirect chain: {redirect_chain}")
    
    final_url = redirect_chain[-1][0]
    expected_param = f"album_id={album.id}"
    if expected_param in final_url:
        print("PASS: Redirected back to filtered album list.")
    else:
        print(f"FAIL: Did not redirect to filtered list. Got: {final_url}")
        
    # Check if image created
    if GalleryImage.objects.filter(album=album, caption="Workflow Test Image").exists():
        print("PASS: Image created in correct album.")
    else:
        print("FAIL: Image not found in database.")

    # Cleanup
    if os.path.exists('test_image_workflow.gif'):
        os.remove('test_image_workflow.gif')
    GalleryImage.objects.filter(album=album).delete()
    album.delete()

if __name__ == "__main__":
    test_album_upload_workflow()
