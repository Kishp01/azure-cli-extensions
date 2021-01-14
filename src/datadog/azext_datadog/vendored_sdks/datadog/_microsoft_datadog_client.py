# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MicrosoftDatadogClientConfiguration
from .operations import MarketplaceAgreementsOperations
from .operations import ApiKeyOperations
from .operations import HostOperations
from .operations import LinkedResourceOperations
from .operations import MonitoredResourceOperations
from .operations import OperationOperations
from .operations import MonitorOperations
from .operations import RefreshSetPasswordOperations
from .operations import TagRuleOperations
from .operations import SingleSignOnConfigurationOperations
from . import models


class MicrosoftDatadogClient(object):
    """MicrosoftDatadogClient.

    :ivar marketplace_agreements: MarketplaceAgreementsOperations operations
    :vartype marketplace_agreements: microsoft_datadog_client.operations.MarketplaceAgreementsOperations
    :ivar api_key: ApiKeyOperations operations
    :vartype api_key: microsoft_datadog_client.operations.ApiKeyOperations
    :ivar host: HostOperations operations
    :vartype host: microsoft_datadog_client.operations.HostOperations
    :ivar linked_resource: LinkedResourceOperations operations
    :vartype linked_resource: microsoft_datadog_client.operations.LinkedResourceOperations
    :ivar monitored_resource: MonitoredResourceOperations operations
    :vartype monitored_resource: microsoft_datadog_client.operations.MonitoredResourceOperations
    :ivar operation: OperationOperations operations
    :vartype operation: microsoft_datadog_client.operations.OperationOperations
    :ivar monitor: MonitorOperations operations
    :vartype monitor: microsoft_datadog_client.operations.MonitorOperations
    :ivar refresh_set_password: RefreshSetPasswordOperations operations
    :vartype refresh_set_password: microsoft_datadog_client.operations.RefreshSetPasswordOperations
    :ivar tag_rule: TagRuleOperations operations
    :vartype tag_rule: microsoft_datadog_client.operations.TagRuleOperations
    :ivar single_sign_on_configuration: SingleSignOnConfigurationOperations operations
    :vartype single_sign_on_configuration: microsoft_datadog_client.operations.SingleSignOnConfigurationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftDatadogClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.marketplace_agreements = MarketplaceAgreementsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_key = ApiKeyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.host = HostOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_resource = LinkedResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitored_resource = MonitoredResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitor = MonitorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.refresh_set_password = RefreshSetPasswordOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tag_rule = TagRuleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.single_sign_on_configuration = SingleSignOnConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MicrosoftDatadogClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)