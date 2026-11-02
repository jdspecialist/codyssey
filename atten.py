import json
import os
from datetime import datetime

# 데이터 파일 이름
DATA_FILE = "attendance.json"

def load_data():
    """파일에서 출석 데이터를 불러옵니다."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    """출석 데이터를 파일에 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_attendance(data):
    """새로운 출석 기록을 추가합니다."""
    print("\n[출석 체크]")
    # 기본값으로 오늘 날짜 제공 (YYYY-MM-DD)
    today = datetime.now().strftime("%Y-%m-%d")
    date = input(f"날짜를 입력하세요 (기본값: {today}): ").strip()
    if not date:
        date = today
        
    name = input("이름을 입력하세요: ").strip()
    
    if name:
        data.append({"date": date, "name": name})
        save_data(data)
        print(f"✅ {name}님의 출석이 완료되었습니다!")
    else:
        print("❌ 이름을 입력해야 합니다.")

def view_attendance(data):
    """전체 출석 목록을 출력합니다."""
    print("\n[출석 목록]")
    if not data:
        print("기록이 없습니다.")
        return
    
    # 날짜순으로 정렬하여 출력
    sorted_data = sorted(data, key=lambda x: x['date'])
    print("-" * 30)
    print(f"{'날짜':<12} | {'이름'}")
    print("-" * 30)
    for entry in sorted_data:
        print(f"{entry['date']:<12} | {entry['name']}")
    print("-" * 30)

def main():
    """메인 메뉴 루프"""
    attendance_data = load_data()
    
    while True:
        print("\n=== 스터디 출석 관리 프로그램 ===")
        print("1. 출석 체크")
        print("2. 출석 목록 보기")
        print("3. 종료")
        choice = input("원하는 메뉴 번호를 선택하세요: ").strip()
        
        if choice == "1":
            add_attendance(attendance_data)
        elif choice == "2":
            view_attendance(attendance_data)
        elif choice == "3":
            print("프로그램을 종료합니다. 열공하세요! 📖")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()