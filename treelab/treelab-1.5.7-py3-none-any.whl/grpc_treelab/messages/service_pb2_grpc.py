# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import treelab.grpc_treelab.messages.service_pb2 as service__pb2


class TreeLabApiServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateWorkspace = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/CreateWorkspace',
        request_serializer=service__pb2.CreateWorkspaceInput.SerializeToString,
        response_deserializer=service__pb2.WorkspaceId.FromString,
        )
    self.UpdateWorkspace = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateWorkspace',
        request_serializer=service__pb2.UpdateWorkspaceInput.SerializeToString,
        response_deserializer=service__pb2.WorkspaceId.FromString,
        )
    self.AddCore = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/AddCore',
        request_serializer=service__pb2.AddCoreInput.SerializeToString,
        response_deserializer=service__pb2.CoreId.FromString,
        )
    self.UpdateCore = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateCore',
        request_serializer=service__pb2.UpdateCoreInput.SerializeToString,
        response_deserializer=service__pb2.CoreId.FromString,
        )
    self.RemoveCore = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveCore',
        request_serializer=service__pb2.RemoveCoreInput.SerializeToString,
        response_deserializer=service__pb2.CoreId.FromString,
        )
    self.AddTable = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/AddTable',
        request_serializer=service__pb2.AddTableInput.SerializeToString,
        response_deserializer=service__pb2.TableId.FromString,
        )
    self.UpdateTableName = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateTableName',
        request_serializer=service__pb2.UpdateTableNameInput.SerializeToString,
        response_deserializer=service__pb2.TableId.FromString,
        )
    self.RemoveTable = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveTable',
        request_serializer=service__pb2.RemoveTableInput.SerializeToString,
        response_deserializer=service__pb2.TableId.FromString,
        )
    self.AddView = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/AddView',
        request_serializer=service__pb2.AddViewInput.SerializeToString,
        response_deserializer=service__pb2.ViewId.FromString,
        )
    self.UpdateView = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateView',
        request_serializer=service__pb2.UpdateViewInput.SerializeToString,
        response_deserializer=service__pb2.ViewId.FromString,
        )
    self.RemoveView = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveView',
        request_serializer=service__pb2.RemoveViewInput.SerializeToString,
        response_deserializer=service__pb2.ViewId.FromString,
        )
    self.AddColumn = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/AddColumn',
        request_serializer=service__pb2.AddColumnInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.UpdateColumn = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateColumn',
        request_serializer=service__pb2.UpdateColumnInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.RemoveColumn = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveColumn',
        request_serializer=service__pb2.RemoveColumnInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.RemoveColumnFromView = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveColumnFromView',
        request_serializer=service__pb2.RemoveColumnFromViewInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.UpdateColumnWidth = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateColumnWidth',
        request_serializer=service__pb2.UpdateColumnWidthInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.ReorderColumn = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/ReorderColumn',
        request_serializer=service__pb2.ReorderColumnInput.SerializeToString,
        response_deserializer=service__pb2.ColumnId.FromString,
        )
    self.AddRow = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/AddRow',
        request_serializer=service__pb2.AddRowInput.SerializeToString,
        response_deserializer=service__pb2.RowId.FromString,
        )
    self.ReorderRow = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/ReorderRow',
        request_serializer=service__pb2.ReorderRowInput.SerializeToString,
        response_deserializer=service__pb2.RowId.FromString,
        )
    self.RemoveRow = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveRow',
        request_serializer=service__pb2.RemoveRowInput.SerializeToString,
        response_deserializer=service__pb2.RowId.FromString,
        )
    self.RemoveRowFromView = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveRowFromView',
        request_serializer=service__pb2.RemoveRowFromViewInput.SerializeToString,
        response_deserializer=service__pb2.RowId.FromString,
        )
    self.UpdateCell = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/UpdateCell',
        request_serializer=service__pb2.UpdateCellInput.SerializeToString,
        response_deserializer=service__pb2.TableId.FromString,
        )
    self.RemoveCell = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/RemoveCell',
        request_serializer=service__pb2.RemoveCellInput.SerializeToString,
        response_deserializer=service__pb2.TableId.FromString,
        )
    self.SubscribeToWorkspace = channel.unary_stream(
        '/co.treelab.api.TreeLabApiService/SubscribeToWorkspace',
        request_serializer=service__pb2.WorkspaceSubscriptionInput.SerializeToString,
        response_deserializer=service__pb2.EventPayload.FromString,
        )
    self.GetWorkspace = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetWorkspace',
        request_serializer=service__pb2.GetWorkspaceInput.SerializeToString,
        response_deserializer=service__pb2.WorkspaceProjection.FromString,
        )
    self.GetCore = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetCore',
        request_serializer=service__pb2.GetCoreInput.SerializeToString,
        response_deserializer=service__pb2.CoreProjection.FromString,
        )
    self.GetTable = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetTable',
        request_serializer=service__pb2.GetTableInput.SerializeToString,
        response_deserializer=service__pb2.TableProjection.FromString,
        )
    self.GetCellByColumnAndRowId = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetCellByColumnAndRowId',
        request_serializer=service__pb2.GetCellByColumnAndRowIdInput.SerializeToString,
        response_deserializer=service__pb2.CellData.FromString,
        )
    self.GetLookupCellByColumnAndRowId = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetLookupCellByColumnAndRowId',
        request_serializer=service__pb2.GetLookupCellByColumnAndRowIdInput.SerializeToString,
        response_deserializer=service__pb2.LookupCellDataResult.FromString,
        )
    self.GetAllWorkspaces = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetAllWorkspaces',
        request_serializer=service__pb2.EmptyInput.SerializeToString,
        response_deserializer=service__pb2.WorkspacesResult.FromString,
        )
    self.GetAllCores = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetAllCores',
        request_serializer=service__pb2.GetCoresInput.SerializeToString,
        response_deserializer=service__pb2.CoresResult.FromString,
        )
    self.GetAllTables = channel.unary_unary(
        '/co.treelab.api.TreeLabApiService/GetAllTables',
        request_serializer=service__pb2.GetTablesInput.SerializeToString,
        response_deserializer=service__pb2.TablesResult.FromString,
        )


class TreeLabApiServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateWorkspace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateWorkspace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddCore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveCore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTableName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddView(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateView(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveView(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddColumn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateColumn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveColumn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveColumnFromView(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateColumnWidth(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReorderColumn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddRow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReorderRow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveRow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveRowFromView(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCell(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveCell(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeToWorkspace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkspace(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTable(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCellByColumnAndRowId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLookupCellByColumnAndRowId(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllWorkspaces(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllCores(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllTables(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TreeLabApiServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateWorkspace': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWorkspace,
          request_deserializer=service__pb2.CreateWorkspaceInput.FromString,
          response_serializer=service__pb2.WorkspaceId.SerializeToString,
      ),
      'UpdateWorkspace': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateWorkspace,
          request_deserializer=service__pb2.UpdateWorkspaceInput.FromString,
          response_serializer=service__pb2.WorkspaceId.SerializeToString,
      ),
      'AddCore': grpc.unary_unary_rpc_method_handler(
          servicer.AddCore,
          request_deserializer=service__pb2.AddCoreInput.FromString,
          response_serializer=service__pb2.CoreId.SerializeToString,
      ),
      'UpdateCore': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCore,
          request_deserializer=service__pb2.UpdateCoreInput.FromString,
          response_serializer=service__pb2.CoreId.SerializeToString,
      ),
      'RemoveCore': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveCore,
          request_deserializer=service__pb2.RemoveCoreInput.FromString,
          response_serializer=service__pb2.CoreId.SerializeToString,
      ),
      'AddTable': grpc.unary_unary_rpc_method_handler(
          servicer.AddTable,
          request_deserializer=service__pb2.AddTableInput.FromString,
          response_serializer=service__pb2.TableId.SerializeToString,
      ),
      'UpdateTableName': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTableName,
          request_deserializer=service__pb2.UpdateTableNameInput.FromString,
          response_serializer=service__pb2.TableId.SerializeToString,
      ),
      'RemoveTable': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveTable,
          request_deserializer=service__pb2.RemoveTableInput.FromString,
          response_serializer=service__pb2.TableId.SerializeToString,
      ),
      'AddView': grpc.unary_unary_rpc_method_handler(
          servicer.AddView,
          request_deserializer=service__pb2.AddViewInput.FromString,
          response_serializer=service__pb2.ViewId.SerializeToString,
      ),
      'UpdateView': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateView,
          request_deserializer=service__pb2.UpdateViewInput.FromString,
          response_serializer=service__pb2.ViewId.SerializeToString,
      ),
      'RemoveView': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveView,
          request_deserializer=service__pb2.RemoveViewInput.FromString,
          response_serializer=service__pb2.ViewId.SerializeToString,
      ),
      'AddColumn': grpc.unary_unary_rpc_method_handler(
          servicer.AddColumn,
          request_deserializer=service__pb2.AddColumnInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'UpdateColumn': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateColumn,
          request_deserializer=service__pb2.UpdateColumnInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'RemoveColumn': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveColumn,
          request_deserializer=service__pb2.RemoveColumnInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'RemoveColumnFromView': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveColumnFromView,
          request_deserializer=service__pb2.RemoveColumnFromViewInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'UpdateColumnWidth': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateColumnWidth,
          request_deserializer=service__pb2.UpdateColumnWidthInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'ReorderColumn': grpc.unary_unary_rpc_method_handler(
          servicer.ReorderColumn,
          request_deserializer=service__pb2.ReorderColumnInput.FromString,
          response_serializer=service__pb2.ColumnId.SerializeToString,
      ),
      'AddRow': grpc.unary_unary_rpc_method_handler(
          servicer.AddRow,
          request_deserializer=service__pb2.AddRowInput.FromString,
          response_serializer=service__pb2.RowId.SerializeToString,
      ),
      'ReorderRow': grpc.unary_unary_rpc_method_handler(
          servicer.ReorderRow,
          request_deserializer=service__pb2.ReorderRowInput.FromString,
          response_serializer=service__pb2.RowId.SerializeToString,
      ),
      'RemoveRow': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveRow,
          request_deserializer=service__pb2.RemoveRowInput.FromString,
          response_serializer=service__pb2.RowId.SerializeToString,
      ),
      'RemoveRowFromView': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveRowFromView,
          request_deserializer=service__pb2.RemoveRowFromViewInput.FromString,
          response_serializer=service__pb2.RowId.SerializeToString,
      ),
      'UpdateCell': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCell,
          request_deserializer=service__pb2.UpdateCellInput.FromString,
          response_serializer=service__pb2.TableId.SerializeToString,
      ),
      'RemoveCell': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveCell,
          request_deserializer=service__pb2.RemoveCellInput.FromString,
          response_serializer=service__pb2.TableId.SerializeToString,
      ),
      'SubscribeToWorkspace': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeToWorkspace,
          request_deserializer=service__pb2.WorkspaceSubscriptionInput.FromString,
          response_serializer=service__pb2.EventPayload.SerializeToString,
      ),
      'GetWorkspace': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkspace,
          request_deserializer=service__pb2.GetWorkspaceInput.FromString,
          response_serializer=service__pb2.WorkspaceProjection.SerializeToString,
      ),
      'GetCore': grpc.unary_unary_rpc_method_handler(
          servicer.GetCore,
          request_deserializer=service__pb2.GetCoreInput.FromString,
          response_serializer=service__pb2.CoreProjection.SerializeToString,
      ),
      'GetTable': grpc.unary_unary_rpc_method_handler(
          servicer.GetTable,
          request_deserializer=service__pb2.GetTableInput.FromString,
          response_serializer=service__pb2.TableProjection.SerializeToString,
      ),
      'GetCellByColumnAndRowId': grpc.unary_unary_rpc_method_handler(
          servicer.GetCellByColumnAndRowId,
          request_deserializer=service__pb2.GetCellByColumnAndRowIdInput.FromString,
          response_serializer=service__pb2.CellData.SerializeToString,
      ),
      'GetLookupCellByColumnAndRowId': grpc.unary_unary_rpc_method_handler(
          servicer.GetLookupCellByColumnAndRowId,
          request_deserializer=service__pb2.GetLookupCellByColumnAndRowIdInput.FromString,
          response_serializer=service__pb2.LookupCellDataResult.SerializeToString,
      ),
      'GetAllWorkspaces': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllWorkspaces,
          request_deserializer=service__pb2.EmptyInput.FromString,
          response_serializer=service__pb2.WorkspacesResult.SerializeToString,
      ),
      'GetAllCores': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllCores,
          request_deserializer=service__pb2.GetCoresInput.FromString,
          response_serializer=service__pb2.CoresResult.SerializeToString,
      ),
      'GetAllTables': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllTables,
          request_deserializer=service__pb2.GetTablesInput.FromString,
          response_serializer=service__pb2.TablesResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'co.treelab.api.TreeLabApiService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
