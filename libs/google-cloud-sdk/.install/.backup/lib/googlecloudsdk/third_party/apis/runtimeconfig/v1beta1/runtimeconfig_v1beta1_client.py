"""Generated client library for runtimeconfig version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.runtimeconfig.v1beta1 import runtimeconfig_v1beta1_messages as messages


class RuntimeconfigV1beta1(base_api.BaseApiClient):
  """Generated client library for service runtimeconfig version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://runtimeconfig.googleapis.com/'

  _PACKAGE = u'runtimeconfig'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloudruntimeconfig']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'RuntimeconfigV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new runtimeconfig handle."""
    url = url or self.BASE_URL
    super(RuntimeconfigV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_configs_operations = self.ProjectsConfigsOperationsService(self)
    self.projects_configs_variables = self.ProjectsConfigsVariablesService(self)
    self.projects_configs_waiters = self.ProjectsConfigsWaitersService(self)
    self.projects_configs = self.ProjectsConfigsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsConfigsOperationsService(base_api.BaseApiService):
    """Service class for the projects_configs_operations resource."""

    _NAME = u'projects_configs_operations'

    def __init__(self, client):
      super(RuntimeconfigV1beta1.ProjectsConfigsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (RuntimeconfigProjectsConfigsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.operations.get',
        ordered_params=[u'projectsId', u'configsId', u'operationsId'],
        path_params=[u'configsId', u'operationsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/operations/{operationsId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (RuntimeconfigProjectsConfigsOperationsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.operations.testIamPermissions',
        ordered_params=[u'projectsId', u'configsId', u'operationsId'],
        path_params=[u'configsId', u'operationsId', u'projectsId'],
        query_params=[u'permissions'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/operations/{operationsId}:testIamPermissions',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsOperationsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsConfigsVariablesService(base_api.BaseApiService):
    """Service class for the projects_configs_variables resource."""

    _NAME = u'projects_configs_variables'

    def __init__(self, client):
      super(RuntimeconfigV1beta1.ProjectsConfigsVariablesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a variable within the given configuration. You cannot create.
a variable with a name that is a prefix of an existing variable name, or a
name that has an existing variable name as a prefix.

To learn more about creating a variable, read the
[Setting and Getting Data](/deployment-manager/runtime-configurator/set-and-get-variables)
documentation.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Variable) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.variables.create',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[u'requestId'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables',
        request_field=u'variable',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesCreateRequest',
        response_type_name=u'Variable',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a variable or multiple variables.

If you specify a variable name, then that variable is deleted. If you
specify a prefix and `recursive` is true, then all variables with that
prefix are deleted. You must set a `recursive` to true if you delete
variables by prefix.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'runtimeconfig.projects.configs.variables.delete',
        ordered_params=[u'projectsId', u'configsId', u'variablesId'],
        path_params=[u'configsId', u'projectsId', u'variablesId'],
        query_params=[u'recursive'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables/{variablesId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a single variable.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Variable) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.variables.get',
        ordered_params=[u'projectsId', u'configsId', u'variablesId'],
        path_params=[u'configsId', u'projectsId', u'variablesId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables/{variablesId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesGetRequest',
        response_type_name=u'Variable',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists variables within given a configuration, matching any provided filters.
This only lists variable names, not the values.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVariablesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.variables.list',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesListRequest',
        response_type_name=u'ListVariablesResponse',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.variables.testIamPermissions',
        ordered_params=[u'projectsId', u'configsId', u'variablesId'],
        path_params=[u'configsId', u'projectsId', u'variablesId'],
        query_params=[u'permissions'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables/{variablesId}:testIamPermissions',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates an existing variable with a new value.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Variable) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'runtimeconfig.projects.configs.variables.update',
        ordered_params=[u'projectsId', u'configsId', u'variablesId'],
        path_params=[u'configsId', u'projectsId', u'variablesId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables/{variablesId}',
        request_field=u'variable',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesUpdateRequest',
        response_type_name=u'Variable',
        supports_download=False,
    )

    def Watch(self, request, global_params=None):
      """Watches a specific variable and waits for a change in the variable's value.
When there is a change, this method returns the new value or times out.

If a variable is deleted while being watched, the `variableState` state is
set to `DELETED` and the method returns the last known variable `value`.

If you set the deadline for watching to a larger value than internal timeout
(60 seconds), the current variable value is returned and the `variableState`
will be `VARIABLE_STATE_UNSPECIFIED`.

To learn more about creating a watcher, read the
[Watching a Variable for Changes](/deployment-manager/runtime-configurator/watching-a-variable)
documentation.

      Args:
        request: (RuntimeconfigProjectsConfigsVariablesWatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Variable) The response message.
      """
      config = self.GetMethodConfig('Watch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Watch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.variables.watch',
        ordered_params=[u'projectsId', u'configsId', u'variablesId'],
        path_params=[u'configsId', u'projectsId', u'variablesId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/variables/{variablesId}:watch',
        request_field=u'watchVariableRequest',
        request_type_name=u'RuntimeconfigProjectsConfigsVariablesWatchRequest',
        response_type_name=u'Variable',
        supports_download=False,
    )

  class ProjectsConfigsWaitersService(base_api.BaseApiService):
    """Service class for the projects_configs_waiters resource."""

    _NAME = u'projects_configs_waiters'

    def __init__(self, client):
      super(RuntimeconfigV1beta1.ProjectsConfigsWaitersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Waiter resource. This operation returns a long-running Operation.
resource which can be polled for completion. However, a waiter with the
given name will exist (and can be retrieved) prior to the operation
completing. If the operation fails, the failed Waiter resource will
still exist and must be deleted prior to subsequent creation attempts.

      Args:
        request: (RuntimeconfigProjectsConfigsWaitersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.waiters.create',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[u'requestId'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/waiters',
        request_field=u'waiter',
        request_type_name=u'RuntimeconfigProjectsConfigsWaitersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the waiter with the specified name.

      Args:
        request: (RuntimeconfigProjectsConfigsWaitersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'runtimeconfig.projects.configs.waiters.delete',
        ordered_params=[u'projectsId', u'configsId', u'waitersId'],
        path_params=[u'configsId', u'projectsId', u'waitersId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/waiters/{waitersId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsWaitersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a single waiter.

      Args:
        request: (RuntimeconfigProjectsConfigsWaitersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Waiter) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.waiters.get',
        ordered_params=[u'projectsId', u'configsId', u'waitersId'],
        path_params=[u'configsId', u'projectsId', u'waitersId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/waiters/{waitersId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsWaitersGetRequest',
        response_type_name=u'Waiter',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """List waiters within the given configuration.

      Args:
        request: (RuntimeconfigProjectsConfigsWaitersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListWaitersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.waiters.list',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/waiters',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsWaitersListRequest',
        response_type_name=u'ListWaitersResponse',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (RuntimeconfigProjectsConfigsWaitersTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.waiters.testIamPermissions',
        ordered_params=[u'projectsId', u'configsId', u'waitersId'],
        path_params=[u'configsId', u'projectsId', u'waitersId'],
        query_params=[u'permissions'],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}/waiters/{waitersId}:testIamPermissions',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsWaitersTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsConfigsService(base_api.BaseApiService):
    """Service class for the projects_configs resource."""

    _NAME = u'projects_configs'

    def __init__(self, client):
      super(RuntimeconfigV1beta1.ProjectsConfigsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a new RuntimeConfig resource. The configuration name must be.
unique within project.

      Args:
        request: (RuntimeconfigProjectsConfigsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RuntimeConfig) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.create',
        ordered_params=[u'projectsId'],
        path_params=[u'projectsId'],
        query_params=[u'requestId'],
        relative_path=u'v1beta1/projects/{projectsId}/configs',
        request_field=u'runtimeConfig',
        request_type_name=u'RuntimeconfigProjectsConfigsCreateRequest',
        response_type_name=u'RuntimeConfig',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a RuntimeConfig resource.

      Args:
        request: (RuntimeconfigProjectsConfigsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'runtimeconfig.projects.configs.delete',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a RuntimeConfig resource.

      Args:
        request: (RuntimeconfigProjectsConfigsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RuntimeConfig) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.get',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsGetRequest',
        response_type_name=u'RuntimeConfig',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (RuntimeconfigProjectsConfigsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.getIamPolicy',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}:getIamPolicy',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all the RuntimeConfig resources within project.

      Args:
        request: (RuntimeconfigProjectsConfigsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConfigsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'runtimeconfig.projects.configs.list',
        ordered_params=[u'projectsId'],
        path_params=[u'projectsId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/projects/{projectsId}/configs',
        request_field='',
        request_type_name=u'RuntimeconfigProjectsConfigsListRequest',
        response_type_name=u'ListConfigsResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (RuntimeconfigProjectsConfigsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.setIamPolicy',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'RuntimeconfigProjectsConfigsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (RuntimeconfigProjectsConfigsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'runtimeconfig.projects.configs.testIamPermissions',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'RuntimeconfigProjectsConfigsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates a RuntimeConfig resource. The configuration must exist beforehand.

      Args:
        request: (RuntimeconfigProjectsConfigsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RuntimeConfig) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'runtimeconfig.projects.configs.update',
        ordered_params=[u'projectsId', u'configsId'],
        path_params=[u'configsId', u'projectsId'],
        query_params=[],
        relative_path=u'v1beta1/projects/{projectsId}/configs/{configsId}',
        request_field=u'runtimeConfig',
        request_type_name=u'RuntimeconfigProjectsConfigsUpdateRequest',
        response_type_name=u'RuntimeConfig',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(RuntimeconfigV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
