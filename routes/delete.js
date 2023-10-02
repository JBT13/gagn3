import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';
import { deleteUser } from '../db/delete/delete.js';

const router = express.Router();

const dbFile = path.join(fileURLToPath(new URL('.', import.meta.url)), '../db/users.db');

// get login page
router.get('/', (req, res) => {
	res.redirect('/');
});


router.post('/', (req, res) => {
    console.log(req.body.userId)
	deleteUser(dbFile, req.body.userId)
    res.redirect('/');
});



export{ router } ;