# Project Phase 3 - Relational Model

#### Team Name - RaIS
- Rahul Goel - 2019111034
- Ishaan Shah - 2019111028
- Sriram Devata - 2019113007

#### ER Diagram to Relational Model -
- We removed the derived attributes from the table as they shouldn't be stored but rather calculated by querying the DB.
- We converted composite attributes to simple columns in the table rather than nesting them.
- We stored 1:1 and 1:N binary relations as foreign keys in the table except for one relationship.
- The binary relationship **Owns** (1:N) was stored as a seperate table rather than as foreign keys. We came to this decision because both sides of the relationship had optional participation and the Foreign
Key column would just have been `NULL` for most of the organistations.
- We converted M:N and N-ary relations to different tables in the relational model.

#### Relational Model to 1st Normal Form -
- We had one multivalued attribute (**Platform**) which shouldn't be present in the 1st normal form. So we created a seperate table linking the **Video Game ID** to the **Platform**.

#### Note
There are no changes in the 2nd Normal Form and the 3rd Normal Form.
