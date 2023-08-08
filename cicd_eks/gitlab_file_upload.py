import subprocess
import os, inspect

file_list=os.listdir(os.getcwd())
current_file = inspect.getfile(inspect.currentframe())
current_file = current_file.split('\\')[-1]

upload_file=str()
for file in file_list:
    if file not in ['.git', current_file]:
        upload_file+=file+' '

remote_add = ["git", "add"]+upload_file.split()
print(remote_add)

def check_remote_origin_exists():
    try:
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, check=True)
        remote_output = result.stdout

        for line in remote_output.splitlines():
            if gitlab_repo_url in line:
                return True
        
        return False
    except subprocess.CalledProcessError as e:
        print(f'Error occurred : {e}')
        return False

try:
    # GitLab 저장소 URL 설정
    gitlab_repo_url = "http://192.168.100.4/root/jenkins_eks.git"

    # 현재 디렉토리에서 Git 저장소 초기화
    if '.git' not in file_list:
        subprocess.run(["git", "init"], check=True)

    # 원격 저장소 추가
    if not check_remote_origin_exists():
        subprocess.run(["git", "remote", "add", "origin", gitlab_repo_url], check=True)

    subprocess.run(["git", 'branch', '-M', 'main'], check=True)

    # 파일들을 Git 저장소에 추가
    subprocess.run(remote_add, check=True)

    # 커밋 메시지 설정
    commit_message = "files upload"

    # 변경 사항 커밋
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # 파일을 GitLab에 푸시
    subprocess.run(["git", "push", "-uf", "origin", "main"], check=True)

    print("Files successfully pushed to GitLab.")

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
