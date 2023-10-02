import Database from 'better-sqlite3';

export const deleteUser = (dbFile, userId) => {
	const db = new Database(dbFile);
	const stmt = db.prepare('DELETE FROM users WHERE id = ?');
	stmt.run(userId);
	db.close();
    return true;
};
