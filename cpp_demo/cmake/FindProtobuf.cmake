# Adds the following targets:
#  protobuf::libprotobuf - Protobuf library
#  protobuf::libprotobuf-lite - Protobuf lite library
#  protobuf::libprotoc - Protobuf Protoc Library
#  protobuf::protoc - protoc executable

# Find the include directory
find_path(PROTOBUF_INCLUDE_DIR google/protobuf/service.h)
mark_as_advanced(PROTOBUF_INCLUDE_DIR)

# The Protobuf library
find_library(PROTOBUF_LIBRARY NAMES protobuf)
mark_as_advanced(PROTOBUF_LIBRARY)
add_library(protobuf::libprotobuf UNKNOWN IMPORTED)
set_target_properties(protobuf::libprotobuf PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES ${PROTOBUF_INCLUDE_DIR}
    INTERFACE_LINK_LIBRARIES pthread
    IMPORTED_LOCATION ${PROTOBUF_LIBRARY}
)

# The Protobuf lite library
find_library(PROTOBUF_LITE_LIBRARY NAMES protobuf-lite)
mark_as_advanced(PROTOBUF_LITE_LIBRARY)
add_library(protobuf::libprotobuf-lite UNKNOWN IMPORTED)
set_target_properties(protobuf::libprotobuf-lite PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES ${PROTOBUF_INCLUDE_DIR}
    INTERFACE_LINK_LIBRARIES pthread
    IMPORTED_LOCATION ${PROTOBUF_LITE_LIBRARY}
)

# The Protobuf Protoc Library
find_library(PROTOBUF_PROTOC_LIBRARY NAMES protoc)
mark_as_advanced(PROTOBUF_PROTOC_LIBRARY)
add_library(protobuf::libprotoc UNKNOWN IMPORTED)
set_target_properties(protobuf::libprotoc PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES ${PROTOBUF_INCLUDE_DIR}
    INTERFACE_LINK_LIBRARIES protobuf::libprotobuf
    IMPORTED_LOCATION ${PROTOBUF_PROTOC_LIBRARY}
)

include(${CMAKE_ROOT}/Modules/FindPackageHandleStandardArgs.cmake)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(Protobuf DEFAULT_MSG
    PROTOBUF_LIBRARY PROTOBUF_INCLUDE_DIR )