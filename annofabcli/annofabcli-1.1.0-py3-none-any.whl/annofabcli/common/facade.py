"""
annofabapiのfacadeクラス
"""

import logging
import time
from typing import Any, Callable, Dict, List, NewType, Optional, Tuple  # pylint: disable=unused-import

import annofabapi
import annofabapi.utils
import more_itertools
from annofabapi.models import OrganizationMember, ProjectId, ProjectMemberRole

logger = logging.getLogger(__name__)


class AnnofabApiFacade:
    """
    AnnofabApiのFacadeクラス。annofabapiの複雑な処理を簡単に呼び出せるようにする。
    """

    #: 組織メンバ一覧のキャッシュ(
    _organization_members: Optional[Tuple[ProjectId, List[OrganizationMember]]] = None

    def __init__(self, service: annofabapi.Resource):
        self.service = service

    @staticmethod
    def get_account_id_last_annotation_phase(task_histories: List[Dict[str, Any]]):
        """
        タスク履歴の最後のannotation phaseを担当したaccount_idを取得する. なければNoneを返す
        Args:
            task_histories:

        Returns:


        """
        annotation_histories = [e for e in task_histories if e["phase"] == "annotation"]
        if len(annotation_histories) > 0:
            last_history = annotation_histories[-1]
            return last_history["account_id"]
        else:
            return None

    @staticmethod
    def get_label_name_en(label: Dict[str, Any]):
        """label情報から英語名を取得する"""
        label_name_messages = label["label_name"]["messages"]
        return [e["message"] for e in label_name_messages if e["lang"] == "en-US"][0]

    def get_project_title(self, project_id: str) -> str:
        """
        プロジェクトのタイトルを取得する
        Returns:
            プロジェクトのタイトル

        """
        project, _ = self.service.api.get_project(project_id)
        return project['title']

    def get_my_account_id(self) -> str:
        """
        自分自身のaccount_idを取得する
        Returns:
            account_id

        """
        account, _ = self.service.api.get_my_account()
        return account['account_id']

    def _get_organization_member_with_predicate(self, project_id: str,
                                                predicate: Callable[[Any], bool]) -> Optional[OrganizationMember]:
        """
        account_idから組織メンバを取得する。
        インスタンス変数に組織メンバがあれば、WebAPIは実行しない。

        Args:
            project_id:
            predicate: 組織メンバの検索条件

        Returns:
            組織メンバ。見つからない場合はNone
        """
        def update_organization_members():
            organization_name = self.get_organization_name_from_project_id(project_id)
            members = self.service.wrapper.get_all_organization_members(organization_name)
            self._organization_members = (project_id, members)

        if self._organization_members is not None:
            if self._organization_members[0] == project_id:
                member = more_itertools.first_true(self._organization_members[1], pred=predicate)
                return member

            else:
                # 別の組織の可能性があるので、再度組織メンバを取得する
                update_organization_members()
                return self._get_organization_member_with_predicate(project_id, predicate)

        else:
            update_organization_members()
            return self._get_organization_member_with_predicate(project_id, predicate)

    def get_organization_member_from_account_id(self, project_id: str, account_id: str) -> Optional[OrganizationMember]:
        """
        account_idから組織メンバを取得する。
        インスタンス変数に組織メンバがあれば、WebAPIは実行しない。

        Args:
            project_id:
            accoaunt_id:

        Returns:
            組織メンバ。見つからない場合はNone
        """
        return self._get_organization_member_with_predicate(project_id, lambda e: e["account_id"] == account_id)

    def get_organization_member_from_user_id(self, project_id: str, user_id: str) -> Optional[OrganizationMember]:
        """
        user_idから組織メンバを取得する。
        インスタンス変数に組織メンバがあれば、WebAPIは実行しない。

        Args:
            project_id:
            user_id:

        Returns:
            組織メンバ
        """
        return self._get_organization_member_with_predicate(project_id, lambda e: e["user_id"] == user_id)

    def get_user_id_from_account_id(self, project_id: str, account_id: str) -> Optional[str]:
        """
        account_idからuser_idを取得する.
        インスタンス変数に組織メンバがあれば、WebAPIは実行しない。

        Args:
            project_id:
            accoaunt_id:

        Returns:
            user_id. 見つからなければNone

        """
        member = self.get_organization_member_from_account_id(project_id, account_id)
        if member is None:
            return None
        else:
            return member.get('user_id')

    def get_account_id_from_user_id(self, project_id: str, user_id: str) -> Optional[str]:
        """
        usre_idからaccount_idを取得する。
        インスタンス変数に組織メンバがあれば、WebAPIは実行しない。

        Args:
            project_id:
            user_id:

        Returns:
            account_id. 見つからなければNone

        """
        member = self.get_organization_member_from_user_id(project_id, user_id)
        if member is None:
            return None
        else:
            return member.get('account_id')

    def get_organization_name_from_project_id(self, project_id: str) -> str:
        """
        project_Idから組織名を取得する。
        """
        organization, _ = self.service.api.get_organization_of_project(project_id)
        return organization["organization_name"]

    def my_role_is_owner(self, project_id: str) -> bool:
        my_member, _ = self.service.api.get_my_member_in_project(project_id)
        return my_member["member_role"] == "owner"

    def contains_anys_role(self, project_id: str, roles: List[ProjectMemberRole]) -> bool:
        """
        自分自身のプロジェクトメンバとしてのロールが、指定されたロールのいずれかに合致するかどうか
        Args:
            project_id:
            roles: ロール一覧

        Returns:
            Trueなら、自分自身のロールが、指定されたロールのいずれかに合致する。

        """
        my_member, _ = self.service.api.get_my_member_in_project(project_id)
        my_role = ProjectMemberRole(my_member["member_role"])
        return my_role in roles

    def _download_annotation_archive_with_waiting(self, project_id: str, dest_path: str,
                                                  download_func: Callable[[str, str], Any], job_access_interval: int,
                                                  max_job_access: int) -> bool:
        def get_latest_job():
            job_list = self.service.api.get_project_job(project_id, query_params={"type": "gen-annotation"})[0]["list"]
            assert len(job_list) == 1
            return job_list[0]

        self.service.api.post_annotation_archive_update(project_id)

        job_access_count = 0
        while True:
            job = get_latest_job()
            job_access_count += 1

            if job["job_status"] == "succeeded":
                logger.debug(f"job_id = {job['job_id']} のジョブが成功しました。ダウンロードを開始します。")
                download_func(project_id, dest_path)
                return True

            elif job["job_status"] == "failed":
                logger.info(f"job_id = {job['job_id']} のジョブが失敗しました。")
                return False

            else:
                # 進行中
                if job_access_count < max_job_access:
                    logger.debug(f"job_id = {job['job_id']} のジョブが進行中です。{job_access_interval}秒間待ちます。")
                    time.sleep(job_access_interval)
                else:
                    logger.debug(f"job_id = {job['job_id']} のジョブに {job_access_interval} アクセスしましたが、完了しませんでした。終了します。")
                    logger.info(f"job_id = {job['job_id']} のジョブが失敗しました。")
                    return False

    def download_latest_full_annotation_archive_with_waiting(self, project_id: str, dest_path: str,
                                                             job_access_interval: int = 60,
                                                             max_job_access: int = 10) -> bool:
        """
        最新のFullアノテーションをダウンロードする。アノテーション情報が最新化するまで、数分待つ。
        Args:
            project_id:
            dest_path:
            job_access_interval: ジョブにアクセスする間隔[sec]
            max_job_access: ジョブに最大何回アクセスするか

        Returns:
            True: ダウンロード成功。False: ダウンロード失敗。
        """

        return self._download_annotation_archive_with_waiting(project_id, dest_path,
                                                              self.service.wrapper.download_full_annotation_archive,
                                                              job_access_interval=job_access_interval,
                                                              max_job_access=max_job_access)

    def download_latest_simple_annotation_archive_with_waiting(self, project_id: str, dest_path: str,
                                                               job_access_interval: int = 60,
                                                               max_job_access: int = 10) -> bool:
        """
        最新のSimpleアノテーションをダウンロードする。アノテーション情報が最新化するまで、数分待つ。
        Args:
            project_id:
            dest_path:
            job_access_interval: ジョブにアクセスする間隔[sec]
            max_job_access: ジョブに最大何回アクセスするか

        Returns:
            True: ダウンロード成功。False: ダウンロード失敗。
        """

        return self._download_annotation_archive_with_waiting(project_id, dest_path,
                                                              self.service.wrapper.download_annotation_archive,
                                                              job_access_interval=job_access_interval,
                                                              max_job_access=max_job_access)

    ##################
    # operateTaskのfacade
    ##################

    def change_operator_of_task(self, project_id: str, task_id: str, account_id: str) -> Dict[str, Any]:
        """
        タスクの担当者を変更する
        Args:
            self:
            project_id:
            task_id:
            account_id:

        Returns:
            変更後のtask情報

        """
        task, _ = self.service.api.get_task(project_id, task_id)

        req = {
            "status": "not_started",
            "account_id": account_id,
            "last_updated_datetime": task["updated_datetime"],
        }
        return self.service.api.operate_task(project_id, task_id, request_body=req)[0]

    def change_to_working_phase(self, project_id: str, task_id: str, account_id: str) -> Dict[str, Any]:
        """
        タスクを作業中に変更する
        Args:
            self:
            project_id:
            task_id:
            account_id:

        Returns:
            変更後のtask情報

        """
        task, _ = self.service.api.get_task(project_id, task_id)

        req = {
            "status": "working",
            "account_id": account_id,
            "last_updated_datetime": task["updated_datetime"],
        }
        return self.service.api.operate_task(project_id, task_id, request_body=req)[0]

    def change_to_break_phase(self, project_id: str, task_id: str, account_id: str) -> Dict[str, Any]:
        """
        タスクを休憩中に変更する
        Returns:
            変更後のtask情報
        """
        task, _ = self.service.api.get_task(project_id, task_id)

        req = {
            "status": "break",
            "account_id": account_id,
            "last_updated_datetime": task["updated_datetime"],
        }
        return self.service.api.operate_task(project_id, task_id, request_body=req)[0]

    def reject_task(self, project_id: str, task_id: str, account_id: str,
                    annotator_account_id: Optional[str] = None) -> Dict[str, Any]:
        """
        タスクを差し戻し、annotator_account_id　に担当を割り当てる。
        Args:
            task_id:
            account_id: 差し戻すときのユーザのaccount_id
            annotator_account_id: 差し戻したあとに割り当てるユーザ。Noneの場合は直前のannotation phase担当者に割り当てる。

        Returns:
            変更あとのtask情報

        """

        # タスクを差し戻す
        task, _ = self.service.api.get_task(project_id, task_id)

        req_reject = {
            "status": "rejected",
            "account_id": account_id,
            "last_updated_datetime": task["updated_datetime"],
        }
        rejected_task, _ = self.service.api.operate_task(project_id, task_id, request_body=req_reject)

        req_change_operator = {
            "status": "not_started",
            "account_id": annotator_account_id,
            "last_updated_datetime": rejected_task["updated_datetime"],
        }
        updated_task, _ = self.service.api.operate_task(project_id, task["task_id"], request_body=req_change_operator)
        return updated_task

    def reject_task_assign_last_annotator(self, project_id: str, task_id: str,
                                          account_id: str) -> Tuple[Dict[str, Any], str]:
        """
        タスクを差し戻したあとに、最後のannotation phase担当者に割り当てる。

        Args:
            task_id:
            account_id: 差し戻すときのユーザのaccount_id

        Returns:
            Tuple[変更後のtask情報, 差し戻したタスクの担当者のaccount_id]

        """

        # タスクを差し戻す
        task, _ = self.service.api.get_task(project_id, task_id)
        last_annotator_account_id = self.get_account_id_last_annotation_phase(task["histories_by_phase"])
        updated_task = self.reject_task(project_id, task_id, account_id, last_annotator_account_id)
        return updated_task, last_annotator_account_id

    def complete_task(self, project_id: str, task_id: str, account_id: str) -> Dict[str, Any]:
        """
        タスクを完了状態にする。
        注意：サーバ側ではタスクの検査は実施されない。
        タスクを完了状態にする前にクライアント側であらかじめ「タスクの自動検査」を実施する必要がある。
        """
        task, _ = self.service.api.get_task(project_id, task_id)

        req = {
            "status": "complete",
            "account_id": account_id,
            "last_updated_datetime": task["updated_datetime"],
        }
        return self.service.api.operate_task(project_id, task_id, request_body=req)[0]
