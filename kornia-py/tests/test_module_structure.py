"""Test the new simplified module structure organization."""
import kornia_rs as K


def test_imgproc_module_exists():
    """Test that imgproc submodule exists and has all image processing functions."""
    assert hasattr(K, 'imgproc')
    # Color functions
    assert hasattr(K.imgproc, 'rgb_from_gray')
    assert hasattr(K.imgproc, 'rgb_from_rgba')
    assert hasattr(K.imgproc, 'rgb_from_bgra')
    assert hasattr(K.imgproc, 'bgr_from_rgb')
    assert hasattr(K.imgproc, 'gray_from_rgb')
    # Enhance functions
    assert hasattr(K.imgproc, 'add_weighted')
    # Histogram functions
    assert hasattr(K.imgproc, 'compute_histogram')
    # Resize functions
    assert hasattr(K.imgproc, 'resize')
    # Warp functions
    assert hasattr(K.imgproc, 'warp_affine')
    assert hasattr(K.imgproc, 'warp_perspective')


def test_icp_module_exists():
    """Test that icp submodule exists and has expected functions and classes."""
    assert hasattr(K, 'icp')
    assert hasattr(K.icp, 'icp_vanilla')
    assert hasattr(K.icp, 'ICPConvergenceCriteria')
    assert hasattr(K.icp, 'ICPResult')


def test_io_module_exists():
    """Test that io submodule exists with all IO functions (no nested submodules)."""
    assert hasattr(K, 'io')
    # Top-level IO functions
    assert hasattr(K.io, 'read_image')
    assert hasattr(K.io, 'read_image_any')
    assert hasattr(K.io, 'ImageDecoder')
    assert hasattr(K.io, 'ImageEncoder')
    
    # All format-specific functions directly in io module
    assert hasattr(K.io, 'read_image_png_u8')
    assert hasattr(K.io, 'write_image_png_u8')
    assert hasattr(K.io, 'read_image_jpeg')
    assert hasattr(K.io, 'write_image_jpeg')
    assert hasattr(K.io, 'read_image_tiff_u8')
    assert hasattr(K.io, 'write_image_tiff_f32')
    assert hasattr(K.io, 'read_image_jpegturbo')
    assert hasattr(K.io, 'write_image_jpegturbo')


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
