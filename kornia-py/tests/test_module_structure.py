"""Test the new module structure organization."""
import kornia_rs as K


def test_color_module_exists():
    """Test that color submodule exists and has expected functions."""
    assert hasattr(K, 'color')
    assert hasattr(K.color, 'rgb_from_gray')
    assert hasattr(K.color, 'rgb_from_rgba')
    assert hasattr(K.color, 'rgb_from_bgra')
    assert hasattr(K.color, 'bgr_from_rgb')
    assert hasattr(K.color, 'gray_from_rgb')


def test_enhance_module_exists():
    """Test that enhance submodule exists and has expected functions."""
    assert hasattr(K, 'enhance')
    assert hasattr(K.enhance, 'add_weighted')


def test_histogram_module_exists():
    """Test that histogram submodule exists and has expected functions."""
    assert hasattr(K, 'histogram')
    assert hasattr(K.histogram, 'compute_histogram')


def test_icp_module_exists():
    """Test that icp submodule exists and has expected functions and classes."""
    assert hasattr(K, 'icp')
    assert hasattr(K.icp, 'icp_vanilla')
    assert hasattr(K.icp, 'ICPConvergenceCriteria')
    assert hasattr(K.icp, 'ICPResult')


def test_io_module_exists():
    """Test that io submodule exists with nested submodules."""
    assert hasattr(K, 'io')
    assert hasattr(K.io, 'read_image')
    assert hasattr(K.io, 'read_image_any')
    assert hasattr(K.io, 'ImageDecoder')
    assert hasattr(K.io, 'ImageEncoder')
    
    # Test nested submodules
    assert hasattr(K.io, 'png')
    assert hasattr(K.io.png, 'read_image_png_u8')
    assert hasattr(K.io.png, 'write_image_png_u8')
    
    assert hasattr(K.io, 'jpeg')
    assert hasattr(K.io.jpeg, 'read_image_jpeg')
    assert hasattr(K.io.jpeg, 'write_image_jpeg')
    
    assert hasattr(K.io, 'tiff')
    assert hasattr(K.io.tiff, 'read_image_tiff_u8')
    assert hasattr(K.io.tiff, 'write_image_tiff_f32')
    
    assert hasattr(K.io, 'jpegturbo')
    assert hasattr(K.io.jpegturbo, 'read_image_jpegturbo')
    assert hasattr(K.io.jpegturbo, 'write_image_jpegturbo')


def test_resize_function_exists():
    """Test that resize function exists at top level (not as a submodule since it's a single function)."""
    assert hasattr(K, 'resize')
    assert callable(K.resize)


def test_warp_module_exists():
    """Test that warp submodule exists and has expected functions."""
    assert hasattr(K, 'warp')
    assert hasattr(K.warp, 'warp_affine')
    assert hasattr(K.warp, 'warp_perspective')


def test_backward_compatibility():
    """Test that all functions are still available at top level for backward compatibility."""
    # Color functions
    assert hasattr(K, 'rgb_from_gray')
    assert hasattr(K, 'rgb_from_rgba')
    assert hasattr(K, 'bgr_from_rgb')
    assert hasattr(K, 'gray_from_rgb')
    
    # Enhance functions
    assert hasattr(K, 'add_weighted')
    
    # Histogram functions
    assert hasattr(K, 'compute_histogram')
    
    # ICP functions and classes
    assert hasattr(K, 'icp_vanilla')
    assert hasattr(K, 'ICPConvergenceCriteria')
    assert hasattr(K, 'ICPResult')
    
    # IO functions and classes
    assert hasattr(K, 'read_image')
    assert hasattr(K, 'read_image_any')
    assert hasattr(K, 'ImageDecoder')
    assert hasattr(K, 'ImageEncoder')
    assert hasattr(K, 'read_image_jpeg')
    assert hasattr(K, 'write_image_jpeg')
    assert hasattr(K, 'read_image_png_u8')
    assert hasattr(K, 'write_image_png_u8')
    
    # Resize functions
    assert hasattr(K, 'resize')
    
    # Warp functions
    assert hasattr(K, 'warp_affine')
    assert hasattr(K, 'warp_perspective')


def test_existing_modules_unchanged():
    """Test that existing modules (image, apriltag) are still available."""
    # Image module
    assert hasattr(K, 'image')
    assert hasattr(K.image, 'ImageSize')
    assert hasattr(K.image, 'PixelFormat')
    assert hasattr(K.image, 'ImageLayout')
    
    # AprilTag module with nested family module
    assert hasattr(K, 'apriltag')
    assert hasattr(K.apriltag, 'DecodeTagsConfig')
    assert hasattr(K.apriltag, 'AprilTagDecoder')
    assert hasattr(K.apriltag, 'family')
    assert hasattr(K.apriltag.family, 'TagFamily')
    assert hasattr(K.apriltag.family, 'TagFamilyKind')
