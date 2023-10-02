import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { selectUsers } from '../db/read/read.js';

const router = express.Router();

const dbFile = path.join(fileURLToPath(new URL('.', import.meta.url)), '../db/users.db');

// get index page
router.get('/', (req, res) => {
	const title = 'Home';
	const users = selectUsers(dbFile);
	res.render('index', { title, users });
});

export { router } ;
