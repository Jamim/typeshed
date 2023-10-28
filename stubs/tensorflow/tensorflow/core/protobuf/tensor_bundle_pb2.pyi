"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.tensor_slice_pb2
import tensorflow.core.framework.types_pb2
import tensorflow.core.framework.versions_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class BundleHeaderProto(google.protobuf.message.Message):
    """Protos used in the tensor bundle module (tf/core/util/tensor_bundle/).

    Special header that is associated with a bundle.

    TODO(zongheng,zhifengc): maybe in the future, we can add information about
    which binary produced this checkpoint, timestamp, etc. Sometime, these can be
    valuable debugging information. And if needed, these can be used as defensive
    information ensuring reader (binary version) of the checkpoint and the writer
    (binary version) must match within certain range, etc.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Endianness:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EndiannessEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[BundleHeaderProto._Endianness.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        LITTLE: BundleHeaderProto._Endianness.ValueType  # 0
        BIG: BundleHeaderProto._Endianness.ValueType  # 1

    class Endianness(_Endianness, metaclass=_EndiannessEnumTypeWrapper):
        """An enum indicating the endianness of the platform that produced this
        bundle.  A bundle can only be read by a platform with matching endianness.
        Defaults to LITTLE, as most modern platforms are little-endian.

        Affects the binary tensor data bytes only, not the metadata in protobufs.
        """

    LITTLE: BundleHeaderProto.Endianness.ValueType  # 0
    BIG: BundleHeaderProto.Endianness.ValueType  # 1

    NUM_SHARDS_FIELD_NUMBER: builtins.int
    ENDIANNESS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    num_shards: builtins.int
    """Number of data files in the bundle."""
    endianness: global___BundleHeaderProto.Endianness.ValueType
    @property
    def version(self) -> tensorflow.core.framework.versions_pb2.VersionDef:
        """Versioning of the tensor bundle format."""
    def __init__(
        self,
        *,
        num_shards: builtins.int | None = ...,
        endianness: global___BundleHeaderProto.Endianness.ValueType | None = ...,
        version: tensorflow.core.framework.versions_pb2.VersionDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["endianness", b"endianness", "num_shards", b"num_shards", "version", b"version"]) -> None: ...

global___BundleHeaderProto = BundleHeaderProto

@typing_extensions.final
class BundleEntryProto(google.protobuf.message.Message):
    """Describes the metadata related to a checkpointed tensor."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    SHARD_ID_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    CRC32C_FIELD_NUMBER: builtins.int
    SLICES_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    """The tensor dtype and shape."""
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    shard_id: builtins.int
    """The binary content of the tensor lies in:
      File "shard_id": bytes [offset, offset + size).
    """
    offset: builtins.int
    size: builtins.int
    crc32c: builtins.int
    """The CRC32C checksum of the tensor bytes."""
    @property
    def slices(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto]:
        """Iff present, this entry represents a partitioned tensor.  The previous
        fields are interpreted as follows:

          "dtype", "shape": describe the full tensor.
          "shard_id", "offset", "size", "crc32c": all IGNORED.
             These information for each slice can be looked up in their own
             BundleEntryProto, keyed by each "slice_name".
        """
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        shard_id: builtins.int | None = ...,
        offset: builtins.int | None = ...,
        size: builtins.int | None = ...,
        crc32c: builtins.int | None = ...,
        slices: collections.abc.Iterable[tensorflow.core.framework.tensor_slice_pb2.TensorSliceProto] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["crc32c", b"crc32c", "dtype", b"dtype", "offset", b"offset", "shape", b"shape", "shard_id", b"shard_id", "size", b"size", "slices", b"slices"]) -> None: ...

global___BundleEntryProto = BundleEntryProto
