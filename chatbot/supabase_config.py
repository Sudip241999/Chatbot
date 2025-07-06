import streamlit as st
from st_supabase_connection import SupabaseConnection

def init_supabase():
    return st.connection(
        "supabase",
        type=SupabaseConnection,
        url="https://tpzknakqbkmxdsdvpxmc.supabase.co",
        key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRwemtuYWtxYmtteGRzZHZweG1jIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3ODExMTQsImV4cCI6MjA2NzM1NzExNH0.kWSVFrNPaFUy_dkXU_J_CEDCCGywvzunkmHvs9PKYBo",
    )
