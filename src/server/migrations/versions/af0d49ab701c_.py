"""empty message

Revision ID: af0d49ab701c
Revises: 
Create Date: 2020-01-10 23:10:49.840235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af0d49ab701c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('challenge_name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('problem_statement', sa.Text(), nullable=False),
    sa.Column('input_format', sa.Text(), nullable=False),
    sa.Column('output_format', sa.Text(), nullable=False),
    sa.Column('difficulty', sa.String(length=20), nullable=False),
    sa.Column('sample_input', sa.Text(), nullable=False),
    sa.Column('sample_output', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('max_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contest_name', sa.String(length=80), nullable=False),
    sa.Column('start', sa.DateTime(timezone=120), nullable=False),
    sa.Column('end', sa.DateTime(), nullable=False),
    sa.Column('details', sa.Text(), nullable=False),
    sa.Column('show_leaderboard', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('start')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('profile_location', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('challenge_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_name', sa.String(length=20), nullable=False),
    sa.Column('time_limit', sa.Integer(), nullable=False),
    sa.Column('memory_limit', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('challenges_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contests_challenges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.Column('contest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_cases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('strength', sa.Float(precision=2), nullable=False),
    sa.Column('visibility', sa.Boolean(), nullable=False),
    sa.Column('input_file', sa.String(length=250), nullable=False),
    sa.Column('output_file', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_contests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('contest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_id'], ['contests.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Text(), nullable=True),
    sa.Column('image_file', sa.String(length=250), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('contest_challenge_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_challenge_id'], ['contests_challenges.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('submissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code_file', sa.String(length=250), nullable=True),
    sa.Column('language_name', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('contest_challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_challenge_id'], ['contests_challenges.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attempts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('max_score', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('contest_challenge_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contest_challenge_id'], ['contests_challenges.id'], ),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('submission_outputs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('output_file', sa.String(length=250), nullable=True),
    sa.Column('time_taken', sa.Integer(), nullable=True),
    sa.Column('memory_taken', sa.Integer(), nullable=True),
    sa.Column('passed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=False),
    sa.Column('test_case_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], ),
    sa.ForeignKeyConstraint(['test_case_id'], ['test_cases.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission_outputs')
    op.drop_table('attempts')
    op.drop_table('submissions')
    op.drop_table('events')
    op.drop_table('users_contests')
    op.drop_table('test_cases')
    op.drop_table('contests_challenges')
    op.drop_table('challenges_tags')
    op.drop_table('challenge_settings')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('contests')
    op.drop_table('challenges')
    # ### end Alembic commands ###
