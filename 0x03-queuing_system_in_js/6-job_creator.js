import kue from 'kue'

const que = kue.createQueue();

const job = {
	phoneNumber: '4153518780',
	message: 'This is the code to verify your account',
};

const pushNotif = que.create('push_notification_code', job).save((err) => {
	if (!err) console.log(`Notification job created: ${pushNotif.id}`);
});

pushNotif.on('complete', () => {
	console.log('Notification job completed');
}).on('failed', () => {
	console.log('Notification job failed');
});
