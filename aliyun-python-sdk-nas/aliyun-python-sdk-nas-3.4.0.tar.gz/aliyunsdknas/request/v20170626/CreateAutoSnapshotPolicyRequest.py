# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateAutoSnapshotPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CreateAutoSnapshotPolicy','NAS')

	def get_TimePoints(self):
		return self.get_query_params().get('TimePoints')

	def set_TimePoints(self,TimePoints):
		self.add_query_param('TimePoints',TimePoints)

	def get_RetentionDays(self):
		return self.get_query_params().get('RetentionDays')

	def set_RetentionDays(self,RetentionDays):
		self.add_query_param('RetentionDays',RetentionDays)

	def get_RepeatWeekdays(self):
		return self.get_query_params().get('RepeatWeekdays')

	def set_RepeatWeekdays(self,RepeatWeekdays):
		self.add_query_param('RepeatWeekdays',RepeatWeekdays)

	def get_FileSystemType(self):
		return self.get_query_params().get('FileSystemType')

	def set_FileSystemType(self,FileSystemType):
		self.add_query_param('FileSystemType',FileSystemType)

	def get_AutoSnapshotPolicyName(self):
		return self.get_query_params().get('AutoSnapshotPolicyName')

	def set_AutoSnapshotPolicyName(self,AutoSnapshotPolicyName):
		self.add_query_param('AutoSnapshotPolicyName',AutoSnapshotPolicyName)