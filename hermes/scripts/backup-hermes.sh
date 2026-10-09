#!/bin/bash
# Backup Konfigurasi Hermes Agent - Full Backup
# Dijalankan setiap 2 hari sekali pukul 23:00 WIB

BACKUP_DIR="/opt/data/backup-hermes-config"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$TIMESTAMP] Mulai proses backup lengkap..."

cd "$BACKUP_DIR"

# 1. Backup konfigurasi Hermes (.hermes directory)
echo "[$TIMESTAMP] Backup .hermes..."
tar -czf hermes-config.tar.gz -C "$HOME" .hermes/ 2>/dev/null

# 2. Backup skill-observations (catatan operasi)
echo "[$TIMESTAMP] Backup skill-observations..."
tar -czf skill-observations.tar.gz -C /opt/data skill-observations/ 2>/dev/null

# 3. Backup memory files (MEMORY.md, USER.md)
echo "[$TIMESTAMP] Backup memory files..."
mkdir -p memory-files
cp /opt/data/MEMORY.md /opt/data/USER.md memory-files/ 2>/dev/null
tar -czf memory-files.tar.gz memory-files/ 2>/dev/null
rm -rf memory-files

# 4. Backup config files (.env, config.yaml, AGENTS.md, SOUL.md)
echo "[$TIMESTAMP] Backup config files..."
mkdir -p config-files
cp /opt/data/.env /opt/data/config.yaml /opt/data/AGENTS.md /opt/data/SOUL.md config-files/ 2>/dev/null
tar -czf config-files.tar.gz config-files/ 2>/dev/null
rm -rf config-files

# 5. Backup platforms (channel configurations)
echo "[$TIMESTAMP] Backup platforms..."
tar -czf platforms.tar.gz -C /opt/data platforms/ 2>/dev/null

# 6. Backup channel directory
echo "[$TIMESTAMP] Backup channel directory..."
cp /opt/data/channel_directory.json . 2>/dev/null

# 7. Backup profiles directory (user profiles)
echo "[$TIMESTAMP] Backup profiles..."
tar -czf profiles.tar.gz -C /opt/data profiles/ 2>/dev/null 2>/dev/null || true

# 8. Databases - separate backup (too large for git, store locally)
# state.db is 416MB, we'll note its location but not include in git
echo "[$TIMESTAMP] Note: Large databases (state.db, projects.db, kanban.db) NOT included in git backup."
echo "[$TIMESTAMP] Please backup these separately: /opt/data/state.db, /opt/data/projects.db, /opt/data/kanban.db"

# Git commit & push
echo "[$TIMESTAMP] Commit & push ke GitHub..."
git add .
git commit -m "backup: $TIMESTAMP" 2>/dev/null
if git push origin master 2>/dev/null; then
    echo "[$TIMESTAMP] Backup berhasil dipush ke GitHub."
else
    echo "[$TIMESTAMP] Gagal push ke GitHub."
fi

echo "[$TIMESTAMP] Proses backup selesai."