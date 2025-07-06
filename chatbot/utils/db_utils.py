import json
from supabase_config import init_supabase

def save_chat(email, chat_name, history):
    supabase = init_supabase()
    supabase.table("chats").upsert({
        "user_email": email,
        "chat_name": chat_name,
        "history": json.dumps(history),
    }).execute()

def load_chats(email):
    supabase = init_supabase()
    data = supabase.table("chats").select("*").eq("user_email", email).execute()
    return {r["chat_name"]: json.loads(r["history"]) for r in data.data} if data.data else {}
    
def delete_chat_db(email, chat_name):
    supabase = init_supabase()
    supabase.table("chats").delete().eq("user_email", email).eq("chat_name", chat_name).execute()
