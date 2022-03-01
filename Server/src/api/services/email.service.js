const transporter = require('../../config/mailer.config');
const ejs = require('ejs');

class EmailService {
    
}

EmailService.sendVerifyMail = (email, verifyString) => {

    let sender = process.env.MAIL_USER;
    ejs.renderFile(__dirname + '/../../views/emails/welcomeEmail.ejs', {
        user_firstname: 'You',
        confirm_link: `https://${process.env.API_HOST}/verify/${verifyString}`
    }).then(function(data) {
        let mailOptions = {
            from: sender,
            to: email,
            subject: 'Welcome to the app',
            html: data
        };
        transporter.sendMail(mailOptions, function(error, info) {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
            }
        });
    });
}

EmailService.sendResetPasswordMail = (email, passwordToken) => {
    let sender = process.env.MAIL_USER;
    ejs.renderFile(__dirname + '/../../views/emails/forgetPassword.ejs', {
        user_firstname: 'You',
        confirm_link: `https://${process.env.API_HOST}/resetPassword?token=${passwordToken}`
    }).then(function(data) {
        let mailOptions = {
            from: sender,
            to: email,
            subject: 'Reset your password',
            text: 'Reset your password',
            html: data
        };
        transporter.sendMail(mailOptions, function(error, info) {
            if (error) {
                console.log(error);
            } else {
                console.log('Email sent: ' + info.response);
            }
        });
    });
}

module.exports = EmailService;
